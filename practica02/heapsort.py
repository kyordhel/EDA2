#!/usr/bin/env python3
# Future imports (Python 2.7 compatibility)
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

def intercambia(A, x, y):
	tmp=A[x]
	A[x]=A[y]
	A[y]=tmp
#end def

def particiona(A, p, r):
	print(A)
	x=A[p]
	print(x)
	i=p
	for j in range(p+1, r+1):
		if A[j] <= x:
			i = i+1
			intercambia(A, i, j)
		#end if
	#end for
	intercambia(A, i, j)
#end def
