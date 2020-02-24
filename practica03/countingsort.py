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
	A=[	8, 7, 3, 6, 9, 8, 5, 8, 4, 6,
		9, 8, 7, 5, 9, 6, 1, 4, 8, 4,
		3, 2, 7, 9, 9, 8, 7, 5, 3, 9,
		9, 5, 7, 6, 5, 6, 7, 8, 9, 9,
		6, 2, 4, 9
	]
	countingSort(A,9)
	print(A)


if __name__ == '__main__':
	main()
