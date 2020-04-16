# !/usr/bin/env python3
# Future imports (Python 2.7 compatibility)
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import re
import sys

class Node:
	# Constructor
	def __init__(self, key=None):
		# the key of the node
		self.key = key

		# The children of the node
		self.p = None      # Parent node
		self.left = None
		self.right = None
	#end def

	def __str__(self):
		return '{}'.format(self.key)
	#end def

	def __repr__(self):
		return '{} => ({}, {})'.format(self.key, self.left, self.right)
	#end def
#end class


class Tree:
	# Constructor
	def __init__(self, root=None):
		if (root is None) or isinstance(root, Node):
			self.root = root
		else:
			self.root = Node(root)
	#end def

	# Methods
	def inorder_walk(self):
		def inorder_walk_rec(node):
			if node is not None:
				inorder_walk_rec(node.left)
				print('{} '.format(node.key), end='')
				inorder_walk_rec(node.right)
		# end def inorder_walk_rec
		inorder_walk_rec(self.root)
		print()
	# end def

	def preorder_walk(self):
		pass
	# end def

	def posorder_walk(self):
		pass
	# end def

	def max(self, node=None):
		if node is None:
			node = self.root
		pass
	# end def

	def min(self, node=None):
		if node is None:
			node = self.root
		pass
	# end def

	def iterative_search(self, key):
		x = self.root
		while (x is not None) and (key != x.key):
			x = x.left if key < x.key else x.right
		return x
	# end def

	def insert(self, key):
		pass
	#end def

	def delete(self, key):
		pass
	#end def

	def __str__(self):
		return repr(self.root)
	#end def

	# Loads a preorder-encoded tree from a file
	@staticmethod
	def from_file( file_path ):
		cc = [ -1 ]
		parts = []
		def read_next():
			cc[0] +=1
			if cc[0] < len(parts) and parts[cc[0]] != 'None':
				nxt = Node(int(parts[cc[0]]))
				nxt.left = read_next()
				nxt.right = read_next()
			else:
				nxt = None
			return nxt
		#end read_next

		with open(file_path, 'r') as fp:
			text = fp.read()
		parts = re.split(r'[\s\n]+', text)
		root = read_next()
		return Tree(root)
	#end def
#end class

def main():
	tree = Tree.from_file('example.tree')
	tree.inorder_walk()
	print(tree.iterative_search(17))
	print(tree.iterative_search(5))
	tree.delete(17)
	tree.insert(5)
	tree.insert(-1)
	tree.inorder_walk()
	tree.preorder_walk()
	tree.posorder_walk()
	print(tree.max(tree.iterative_search(5)))
	print(tree.min(tree.iterative_search(5)))


if __name__ == "__main__":
	main()
