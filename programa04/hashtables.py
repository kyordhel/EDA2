# !/usr/bin/env python3
# Future imports (Python 2.7 compatibility)
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import time

class HashTable:

	def __init__(self, m = 5):
		self.T = [None]*m
		for i in range(0, m):
			self.T[i] = []
		self.m = m
		self.longest_list = 0

	def _hash(self, value):
		i = len(value) -1
		wsum = 0
		while i >= 0:
			wsum += ord(value[i]) * i
			i -= 1
		return wsum % self.m

	def insert(self, value):
		if not isinstance(value, str) or len(value.strip()) < 1:
			return
		h = self._hash(value)
		lst = self.T[h]
		# print('      Adding {} with hash {} to {}'.format(value, h, lst))
		i = 0
		while i < len(lst):
			if lst[i] == value:
				print('{} is already in the dictionary'.format(value))
				return
			i += 1
		lst.append(value)
		self.longest_list = max(self.longest_list, i)

	def delete(self, value):
		if not isinstance(value, str) or len(value.strip()) < 1:
			return False
		h = self._hash(value)
		lst = self.T[h]
		i = 0
		while i < len(lst):
			if lst[i] == value:
				del lst[i]
				return True
			i += 1
		return False

	def search(self, value):
		if not isinstance(value, str) or len(value.strip()) < 1:
			return False
		h = self._hash(value)
		lst = self.T[h]
		i = 0
		while i < len(lst):
			if lst[i] == value:
				return True
			i += 1
		return False


def main():
	hashTable = HashTable(5)
	with open('words.txt', 'r') as fp:
		lines = fp.readlines()

	print('Populating dictionary with radix={}'.format(hashTable.m))
	start_time = time.time()
	for line in lines:
		hashTable.insert(line.strip())
		elapsed = 1000 * (time.time() - start_time)
	print('    Longest list size: {} elements'.format( hashTable.longest_list ))
	print('    Elapsed: {} milliseconds'.format( elapsed ))
	print()

	while True:
		try:
			word = input('Type a word to search: ').strip().lower()
			print('    Searching for {}...'.format(word), end='')
			start_time = time.time()
			found = hashTable.search(word)
			elapsed = 1000 * (time.time() - start_time)
			print('\r    {}. Search took {} milliseconds'.format('Found' if found else 'Not found', elapsed ))

		except KeyboardInterrupt:
			print()
			return




if __name__ == "__main__":
	main()
