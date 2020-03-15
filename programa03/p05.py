# !/usr/bin/env python3
# Future imports (Python 2.7 compatibility)
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


def formarTabla(m):
	T=[None]*m
	return T

def convertirLlave(x):
	keyNum = 0
	i = 0
	for char in x:
		keyNum += ord(char)*i
		i+=1
	return keyNum

def h(x, m):
	return x % m

def insertar(T, m, x, valor):
	j = 0
	h1 = h(convertirLlave(x), m)
	while(j < m):
		indice = (h1+j)%m
		par=[x, valor]
		if T[indice] == None:
			T[indice] = par
			return indice
		else:
			j+=1
	print("No hay lugar")
	return -1

def buscar(T, m, x, valor):
	j = 0
	h1 = h(convertirLlave(x), m)
	while(j < m):
		indice = (h1+j)%m
		if T[indice] != None:
			if T[indice][0] == x:
				return indice
			else:
				j+=1
		return -1
	return -1


def main():
	m = 5
	T = formarTabla(m)
	print(T)
	insertar(T, m, "Hola1", "12213291")
	insertar(T, m, "Hola2", "12213292")
	insertar(T, m, "Hola3", "12213293")
	insertar(T, m, "Hola4", "12213294")
	insertar(T, m, "Hola5", "12213295")
	insertar(T, m, "Hola6", "12213296")

	print(T)
	print(buscar(T, m, "Hola5", "12213295"))


if __name__ == "__main__":
	main()
