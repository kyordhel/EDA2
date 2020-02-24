#!/usr/bin/env python3
# Future imports (Python 2.7 compatibility)
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import re
import sys


def radixSort(A):
	for i in range(len(A[0])-1, -1, -1):
		A = countingSort2(A, i)
		print(A)

def countingSort2(A, place, k=256):
	count=[ 0 for i in range(0, k+1) ]
	output=[ 0 for i in range(0, len(A)) ]

	for i in range(0, len(A)):
		count[ord(A[i][place])]+= 1

	for i in range(1, k+1):
		count[i]+= count[i-1]

	for i in range(len(A)-1, -1, -1):
		output[count[ord(A[i][place])]-1] = A[i]
		count[ord(A[i][place])]-=1

	return output

def main():
	A=[	'XI7FS6', 'PL4ZQ2', 'JI8FR9',
		'XL8FQ6', 'PY2ZR5', 'KV7WS9',
		'JL2ZV3', 'KI4WR2'
	]
	print(A)
	radixSort(A)



if __name__ == '__main__':
	main()
