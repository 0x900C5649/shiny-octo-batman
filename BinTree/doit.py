#! /usr/bin/env python 
import sys

str = sys.argv[1]
list = eval(str)
if (len(list) != 12):
	print "ungültige eingabe"
	return

print "\\tikzset{treenode/.style = {align=center, inner sep=0pt, text centered, font=\\sffamily},arn_n/.style = {treenode, circle, white, font=\\sffamily\\bfseries, draw=black,fill=black, text width=1.5em},% arbre rouge noir, noeud noir arn_r/.style = {treenode, circle, red, draw=red, text width=1.5em, very thick},% arbre rouge noir, noeud rouge arn_x/.style = {treenode, rectangle, draw=black, minimum width=0.5em, minimum height=0.5em}% arbre rouge noir, nil}"

print "\\node [arn_n](n1) {}child{ node [arn_n](n2) {} child{ node [arn_n](n4) {} child{ node [arn_n](n8) {}}child{ node [arn_n](n9) {}}}child{ node [arn_n](n5) {}child{ node [arn_n](n10) {}}child{ node [arn_n](n11) {}}}}child{ node [arn_n](n3) {}child{ node [arn_n](n6) {} child{ node [arn_n](n12) {}}child{ node [arn_x] {}}}child{ node [arn_n](n7) {}child{ node [arn_x] {}}child{ node [arn_x] {}}}};"

for i in range (0,12):
	print "\\node at (n" +i +") {\\sffamily{\\textcolor{white}"+list[i]"}};"

#print "\\section*{Hello World} \n"
#print "$"+ str + "$ \\\\"
#a = 0
#for i in list:
#	a = a + i
#print a