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

def busqueda_lineal(A, x):
	i = 0
	for i in range(0, len(A)):
		if A[i] == x:
			return i
	return -1


def main():
	A = [x for x in range(10000000, 0, -1)]
	t0 = time.time()
	print('Buscando 1 en A...')
	indice = busqueda_lineal(A, 1)
	t1 = time.time()
	if indice >= 0:
		print('  Se encontró a 1 en la posición {}'.format(indice))
	else:
		print('  No se encontró a 1 en A')

	print('Buscar 1 en A tomó {0:.4f} milisegundos'.format((t1-t0)*1000))


if __name__ == '__main__':
	main()
