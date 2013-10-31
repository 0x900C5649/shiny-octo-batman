#! /usr/bin/env python 
import sys

print "\\section*{Hello World} \n"
str = sys.argv[1]
print "$"+ str + "$ \\\\"
list = eval(str)
a = 0
for i in list:
	a = a + i
print a