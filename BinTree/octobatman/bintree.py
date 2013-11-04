#! /usr/bin/env python 
import sys

stri = sys.argv[1]
list = eval(stri)
if (len(list) != 12):
	print "ungueltige eingabe"
else:
	print "\\begin{tikzpicture}[-,>=stealth',level/.style={sibling distance = 5cm/#1,level distance = 1.5cm}]" 
	print "\\node [arn_n](n1) {}child{ node [arn_n](n2) {} child{ node [arn_n](n4) {} child{ node [arn_n](n8) {}}child{ node [arn_n](n9) {}}}child{ node [arn_n](n5) {}child{ node [arn_n](n10) {}}child{ node [arn_n](n11) {}}}}child{ node [arn_n](n3) {}child{ node [arn_n](n6) {} child{ node [arn_n](n12) {}}child{ node [arn_x] {}}}child{ node [arn_n](n7) {}child{ node [arn_x] {}}child{ node [arn_x] {}}}};\n"

	for i in range (0,12):
		print '\\node at (n' + str(i+1) +') {\\sffamily{\\textcolor{white}{'+ str(list[i]) +'}}};'
	print "\\end{tikzpicture}"
#print "\\section*{Hello World} \n"
#print "$"+ str + "$ \\\\"
#a = 0
#for i in list:
#	a = a + i
#print a