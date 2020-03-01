#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ## #############################################################
#
# Author: Mauricio Matamoros
# Date:
#
# ## #############################################################
# Future imports (Python 2.7 compatibility)
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys
import time

def busqueda_binaria(A, x, first=-1, last=-1):
	if first == -1:
		first = 0
	if last == -1:
		last = len(A)

	while True:
		if last - first < 0:
			return -1

		mid = int((last - first)/2)
		if x == A[mid]:
			return mid
		elif x > A[mid]:
			first = mid
		elif x < A[mid]:
			last = mid

def busqueda_binaria_recursiva(A, x, first=-1, last=-1):
	if first == -1:
		first = 0
	if last == -1:
		last = len(A)
	mid = int((last - first)/2)
	if x == A[mid]:
		return mid
	elif x > A[mid]:
		return busqueda_binaria_recursiva(A, x, mid, last)
	elif x < A[mid]:
		return busqueda_binaria_recursiva(A, x, first, mid)
	else:
		return -1


def main():
	A = [x for x in range(0, 10000000)]
	t0 = time.time()
	print('Buscando 1 en A...')
	indice = busqueda_binaria(A, 1)
	# indice = busqueda_binaria_recursiva(A, 1)
	t1 = time.time()
	if indice >= 0:
		print('  Se encontró a 1 en la posición {}'.format(indice))
	else:
		print('  No se encontró a 1 en A')

	print('Buscar 1 en A tomó {0:.4f} milisegundos'.format((t1-t0)*1000))


if __name__ == '__main__':
	main()
