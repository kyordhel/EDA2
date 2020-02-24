#!/usr/bin/env python3
# Future imports (Python 2.7 compatibility)
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import re
import sys

def countingSort(A, k):
	count=[ 0 for i in range(0, k+1) ]
	output=[ 0 for i in range(0, len(A)) ]

	for i in range(0, len(A)):
		count[A[i]]+= 1
	print(count)

	for i in range(1, k+1):
		count[i]+= count[i-1]
	print(count)

	for i in range(len(A)-1, -1, -1):
		output[count[A[i]]-1] = A[i]
		count[A[i]]-=1

def main():
	A=[	1, 2, 2, 3, 3, 3, 4, 4, 4, 4,
		5, 5, 5, 5, 5, 6, 6, 6, 6, 6,
		6, 7, 7, 7, 7, 7, 7, 7, 8, 8,
		8, 8, 8, 8, 8, 8, 9, 9, 9, 9,
		9, 9, 9, 9, 9
	]
	countingSort(A,9)
	print(A)


if __name__ == '__main__':
	main()
