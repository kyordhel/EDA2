# !/usr/bin/env python3
# Future imports (Python 2.7 compatibility)
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import re
import sys

class Vertex:
	# Constructor
	def __init__(self, name, neighbors = []):
		self._name = name
		# list of neighbors of this vertex (aka edges)
		self._neighbors = list(neighbors)
		# Misc info used only by the bfs algorithm
		# self.color = 'WHITE'
		# self.d = -1
		# self.p = None
	#end def

	@property
	def name(self):
		return self._name
	#end def

	@property
	def neighbors(self):
		return self._neighbors
	#end def

	def __str__(self):
		return '{} = {}'.format(self._name, ', '.join([n.name for n in self._neighbors]))
	#end def

	def __repr__(self):
		info = ''
		if 'color' in self.__dict__:
			info = ' ({}, d={}, p={})'.format(self.color, self.d, self.p.name if self.p != None else '')
		return '{}{} = {}'.format(self._name, info, ', '.join([n.name for n in self._neighbors]))
	#end def
#end class


class Graph:
	# Constructor
	def __init__(self, vertexes = [] ):
		self._vertexes = list(vertexes)
	#end def

	@property
	def vertexes(self):
		return self._vertexes
	#end def

	def __getitem__(self, key):
		matches = [ vertex for vertex in self.vertexes if vertex.name == key ]
		if len(matches) == 1:
			return matches[0]
		elif len(matches) > 1:
			return matches
		return None

	#end def

	def __str__(self):
		return '\n'.join([ v.__str__() for v in self._vertexes ])
	#end def

	def __repr__(self):
		return '\n'.join([ v.__repr__() for v in self._vertexes ])
	#end def

	# Loads a graph from an adjacency-list file
	@staticmethod
	def from_file( file_path ):
		graph = Graph()
		vertexes = {}
		line_num = 0
		with open(file_path, 'r') as fp:
			line = fp.readline()
			while line:
				# Each line contains a comma-separated list of neighbors
				# e.g. a =  b, c, d
				parts = re.split(r'\s*[\:\=]\s*', line.strip())
				vertex_name = parts[0]
				vertex_nix = re.split(r'\s*,\s*', parts[1])
				if vertex_name in vertexes:
					raise Exception('Duplicated vertex {} declared in line {}'.format(vertex_name, line_num))
				vertexes[vertex_name] = (Vertex(vertex_name), vertex_nix)
				line_num += 1
				line = fp.readline()
		# Perform a concistency check after loading the adjacency list
		# While doing it, the object is structured
		for pair in vertexes.values():
			vobj, vnix = pair
			for n in vnix:
				if not n in vertexes:
					raise Exception('Vertex {} is connected to {} but was not declared (incomplete graph)'.format(n, v))
				vobj.neighbors.append(vertexes[n][0])
			graph.vertexes.append(vobj)
		# Finally we return the graph object
		return graph
	#end def
#end class

time = 0
def dfs(graph):
	global time
	time = 0

	def dfs_visit(graph, u):
		global time
		time = time + 1
		u.d = time
		u.color = 'GRAY'
		for v in u.neighbors:
			if v.color == 'WHITE':
				v.p = u
				dfs_visit(graph, v)
		u.color = 'BLACK'
		time = time + 1
		u.f = time
	#end dfs-visit

	for u in graph.vertexes:
		u.color = 'WHITE'
		u.p = None

	for u in graph.vertexes:
		if u.color == 'WHITE':
			dfs_visit(graph, u)

#end def

def main():
	graph = Graph.from_file('example.graph')
	print(graph)
	dfs(graph)
	print(repr(graph))

if __name__ == "__main__":
	main()
