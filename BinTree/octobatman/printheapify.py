#! /usr/bin/env python 
import sys
import math

def printHeap(list):
	if (len(list) != 12):
		print "ungueltige eingabe"
	else:
		print "\\node [arn_n](n1) {}child{ node [arn_n](n2) {} child{ node [arn_n](n4) {} child{ node [arn_n](n8) {}}child{ node [arn_n](n9) {}}}child{ node [arn_n](n5) {}child{ node [arn_n](n10) {}}child{ node [arn_n](n11) {}}}}child{ node [arn_n](n3) {}child{ node [arn_n](n6) {} child{ node [arn_n](n12) {}}child{ node [arn_x] {}}}child{ node [arn_n](n7) {}child{ node [arn_x] {}}child{ node [arn_x] {}}}};\n"

		for i in range (0,12):
			print '\\node at (n' + str(i+1) +') {\\sffamily{\\textcolor{white}{'+ str(list[i]) +'}}};'


def swap(A, r, l):
	buf = A[r-1]
	A[r-1] = A[l-1]
	A[l-1] = buf

def parent(i):
	return math.ceil(i/2) -1

def left(i): 
	return 2*i
	
def right(i):
	return 2*i+1

def heapify(A, i):
	l = left(i)
	#print "l : $"+ str(l) + "$\\\\"
	r = right(i)
	#print "r : $"+ str(r) + "$\\\\"
	h = i
	#print "h : $"+ str(h) + "$\\\\"
	if(l >len(A) and r >len(A)):
		print "\\begin{tikzpicture}[-,>=stealth',level/.style={sibling distance = 5cm/#1,level distance = 1.5cm}]"
		printHeap(A)
		print "\\end{tikzpicture}"
	else:
		if(l<=len(A) and A[l-1]>A[i-1]):
			h = l
		if(r<=len(A) and A[r-1]>A[h-1]):
			h = r
		if(h!=i):
			swap(A,i,h)
			print "\\begin{tikzpicture}[-,>=stealth',level/.style={sibling distance = 5cm/#1,level distance = 1.5cm}]" 
			printHeap(A)
			if(h == r):
				print "\\draw[<->] (n"+ str(i) + ") to [bend left=30] (n"+str(h)+");"
			else:
				print "\\draw[<->] (n"+ str(i) + ") to [bend right=30] (n"+str(h)+");"
			print "\\end{tikzpicture}\\\\"
			#print "h : $"+ str(h) + "$\\\\"
			heapify(A, h)
		else:
			print "\\begin{tikzpicture}[-,>=stealth',level/.style={sibling distance = 5cm/#1,level distance = 1.5cm}]"
			printHeap(A)
			print "\\end{tikzpicture}\\\\"
		
stri = sys.argv[1]
c = int(sys.argv[2])
list = eval(stri)
heapify(list, c)
