#!/usr/bin/env python
# -*- coding: utf-8 -*-
print """
#####################
#   Caesar Cipher   #
#       v1.0        #
#      h4yuc3       #
#####################
"""
def getValue():
	return raw_input('Enter for decrypt : ')


def Solver(text):
	solved = ''
	Key = 0
	while Key < 26:
		Key=Key+1
		for char in text:
			if char.isalpha():
				num = ord(char)
				num += Key
				
				if char.isupper():
					if num > ord('Z'):
						num -= 26
					elif num < ord('A'):
						num += 26
				elif char.islower():
					if num > ord('z'):
						num -= 26
					elif num < ord('a'):
						num += 26
				solved += chr(num)
			else:
				solved += char
		solved += (' [%s] \n' %Key)
	return solved
		
text = getValue()	
print(Solver(text))
