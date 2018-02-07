import sys
import numpy as np
import math

arg=sys.argv
data={}
curr_chr=''

f_norm=open(arg[1], 'r')
f_targ=open(arg[2], 'r')
f_except=open(arg[2].replace('.bam.txt','').replace('.pref.txt','')+'except.txt', 'w')

line=f_norm.readline()
while line!= '':
	colm=line.strip().split()
	if colm[0]!=curr_chr:
		
		data[colm[0]]=[colm[1]]
		curr_chr=colm[0]
		line=f_norm.readline()
		continue
	data[colm[0]].append(colm[1])
	line=f_norm.readline()

line=f_targ.readline()
while line!= '':
	colm=line.strip().split()
	if colm[1] in data[colm[0]]:
		f_except.write(line)
	line=f_targ.readline()
f_norm.close()
f_targ.close()
f_except.close()
