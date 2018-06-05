# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4
"""
Based on parsepbf.py by Chris Hill <osm@raggedred.net> and osmnodepbf
by Praneeth Bodduluri <lifeeth@gmail.com>.

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
"""
__author__ = 'Joe Nudell'
__email__ = 'joenudell@gmail.com'


import osmformat_pb2
import fileformat_pb2
from struct import unpack
import zlib



class Parser(object):
    """This class helps parse the pbf file for nodes with the specified tags"""

    def __init__(self, filename):
        """Initialize the class with the filename of the pbf you want to parse"""
        self.filename = filename
        self.tags = {}    # content is {key: set(values)}, ...
        self.nodes = []
        if getattr(self, 'fpbf', None):
            self.fpbf.close()
        self.fpbf = open(self.filename, 'rb')
        self.blobhead = fileformat_pb2.BlobHeader()
        self.blob = fileformat_pb2.Blob()
        self.hblock = osmformat_pb2.HeaderBlock()
        self.primblock = osmformat_pb2.PrimitiveBlock()
        self.membertype = {0: 'node', 1: 'way', 2: 'relation'}
        if not self._read_pbf_blob_header():
            return False
        #read the blob
        if not self._read_blob():
            return False
        #check the contents of the first blob are supported
        self.hblock.ParseFromString(self.BlobData)
        for rf in self.hblock.required_features:
            if rf in {"OsmSchema-V0.6","DenseNodes"}:
                pass
            else:
                raise TypeError("not a required feature %s" % rf )

    def __del__(self):
        self.fpbf.close()

    def return_tags(self, refresh = False):
        """Returns all the keyvalue pairs in the tag list"""
        if len(self.tags) == 0 or refresh:
            self.parse(refresh = True)
        return self.tags

    def parse(self, tag = None, refresh = False):
        """This parses the pbf for nodes for the given tags"""
        if tag is None:
            tag = {}
        if refresh:
            self.__init__(self.filename)
        while self._read_next_block():
            for pg in self.primblock.primitivegroup:
                if len(pg.nodes) > 0:
                    self._process_nodes(pg.nodes, tag)
                if len(pg.dense.id) > 0:
                    self._process_dense(pg.dense, tag)
        return self.nodes

    def _read_pbf_blob_header(self):
        """Read a blob header, store the data for later"""
        size = self._readint()
        if size <= 0:
            return False

        if not self.blobhead.ParseFromString(self.fpbf.read(size)):
            return False
        return True

    def _read_blob(self):
        """Get the blob data, store the data for later"""
        size = self.blobhead.datasize
        if not self.blob.ParseFromString(self.fpbf.read(size)):
            return False
        if self.blob.raw_size > 0:
            # uncompress the raw data
            self.BlobData = zlib.decompress(self.blob.zlib_data)
            #print "uncompressed BlobData %s"%(self.BlobData)
        else:
            #the data does not need uncompressing
            self.BlobData = raw
        return True

    def _read_next_block(self):
        """read the next block. Block is a header and blob, then extract the block"""
        # read a BlobHeader to get things rolling. It should be 'OSMData'
        if not self._read_pbf_blob_header():
            return False
        if self.blobhead.type != "OSMData":
            print("Expected OSMData, found %s"%(self.blobhead.type))
            return False
            # read a Blob to actually get some data
        if not self._read_blob():
            return False
        # extract the primative block
        self.primblock.ParseFromString(self.BlobData)
        return True

    def _readint(self):
        """read an integer in network byte order and change to machine byte order. Return -1 if eof"""
        be_int = self.fpbf.read(4)
        if len(be_int) == 0:
            return -1
        else:
            le_int = unpack('!L', be_int)
            return le_int[0]

    def _process_nodes(self, nodes, tag = None):
        """This process the nodes adding the ones with the requested tag to a list"""
        if not tag:
            tag = {}
        tset = set(tag.keys())
        NANO = 1000000000
        found_tag = False
        gran = float(self.primblock.granularity)
        latoff = float(self.primblock.lat_offset)
        lonoff = float(self.primblock.lon_offset)
        for nd in nodes:
            node = {}
            node["tag"] = {}
            for i in range(len(nd.keys)):
                ky = nd.keys[i]
                vl = nd.vals[i]
                sky = self.primblock.stringtable.s[ky] #Key
                svl = self.primblock.stringtable.s[vl] #Value
                if sky in node['tag']:
                    if type(node['tag'][sky]) is not list:
                        node['tag'][sky] = [node['tag'][sky]]
                    node['tag'][sky].append(svl)
                else:
                    node['tag'][sky] = svl
                if sky in tag:
                    if "*" in tag[sky] or svl in tag[sky]:
                        found_tag = True
                if not tag:
                    if sky in self.tags:
                        self.tags[sky].add(svl)
                    else:
                        self.tags[sky] = set([svl])
                    found_tag = True
            if found_tag:
                node["nodeid"] = nd.id
                node["lat"] = float(nd.lat * gran + latoff) / NANO
                node["lon"] = float(nd.lon * gran + lonoff) / NANO
                node["vs"] = nd.info.version
                node["ts"] = nd.info.timestamp
                node["uid"] = nd.info.uid
                node["user"] = nd.info.user_sid
                node["cs"] = nd.info.changeset
                node["tm"] = ts * self.primblock.date_granularity / 1000
                self.nodes.append(node)
                found_tag = False

    def _process_dense(self, dense, tag = None):
        """process a dense node block"""
        if not tag:
            tag = {}
        NANO = 1000000000
        found_tag = False
        #DenseNode uses a delta system of encoding os everything needs to start at zero
        lastID = 0
        lastLat = 0
        lastLon = 0
        tagloc = 0
        cs = 0
        ts = 0
        uid = 0
        user = 0
        gran = float(self.primblock.granularity)
        latoff = float(self.primblock.lat_offset)
        lonoff = float(self.primblock.lon_offset)
        for i in range(len(dense.id)):
            node = {}
            node["tag"] = {}
            lastID += dense.id[i]
            lastLat += dense.lat[i]
            lastLon += dense.lon[i]
            lat = float(lastLat * gran + latoff) / NANO
            lon = float(lastLon * gran + lonoff) / NANO
            user += dense.denseinfo.user_sid[i]
            uid += dense.denseinfo.uid[i]
            vs = dense.denseinfo.version[i]
            ts += dense.denseinfo.timestamp[i]
            cs += dense.denseinfo.changeset[i]
            suser = self.primblock.stringtable.s[user]
            tm = ts * self.primblock.date_granularity / 1000
            if tagloc < len(dense.keys_vals):  # don't try to read beyond the end of the list
                while dense.keys_vals[tagloc] != 0:
                    ky = dense.keys_vals[tagloc]
                    vl = dense.keys_vals[tagloc + 1]
                    tagloc += 2
                    sky = self.primblock.stringtable.s[ky] #Key
                    svl = self.primblock.stringtable.s[vl] #Value
                    if sky in node['tag']:
                        if type(node['tag'][sky]) is not list:
                            node['tag'][sky] = [node['tag'][sky]]
                        else:
                            node['tag'][sky].append(svl)
                    else:
                        node['tag'][sky] = svl
                    if sky in tag:
                        if "*" in tag[sky] or svl in tag[sky]:
                            found_tag = True
                    if not tag:
                        if sky in self.tags:
                            self.tags[sky].add(svl)
                        else:
                            self.tags[sky] = set([svl])
                        found_tag = True
            tagloc += 1
            if found_tag:
                node["nodeid"] = lastID
                node["lon"] = lon
                node["lat"] = lat
                node["user"] = suser
                node["uid"] = uid
                node["version"] = vs
                node["changeset"] = cs
                node["time"] = tm
                self.nodes.append(node)
                found_tag = False

