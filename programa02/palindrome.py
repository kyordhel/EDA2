# !/usr/bin/env python3
# Future imports (Python 2.7 compatibility)
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

def isPalindrome(s):
	# Ignora cualquier entrada que no sea una cadena
	if not isinstance(s, str):
		return False
	i = 0;
	j = len(s) -1;
	# Compara el principio con el final de la cadena
	while i < j:
		if s[i] != s[j]:
			return False
		i+=1
		j+=1
	return True

def main():
	while True:
		try:
			word = input("Escriba una palabra: ")
			if isPalindrome(word):
				print('{} es un palindromo'.format(word))
			else:
				print('{} no es un palindromo'.format(word))
		except KeyboardInterrupt:
			print()
			return


if __name__ == "__main__":
	main()
