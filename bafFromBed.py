import sys
import numpy as np
import math

arg=sys.argv
data=[]
#lable=True
f_cvf=open(arg[1], 'r')
f_baf=open(arg[1]+'baf.txt', 'w')
step=10000
delcoin=0
line=f_cvf.readline()
while line!= '':
	if line[0]=='#':
		line=f_cvf.readline()
		continue
	data=[]
	lable_data=np.array([[0,0]])
	if line=='':
		break
	colm=line.strip().split('\t')
	if colm[5]=='0':
		line=f_cvf.readline()
		continue
	colm[0]=colm[0].replace('chr','').replace('X', '23').replace('Y', '24').replace('M', '25')

	f_baf.write(str(colm[0])+'\t'+str(colm[2])+'\t'+str(colm[3])+'\t'+str(colm[4])+'\n')
	line=f_cvf.readline()
f_cvf.close()
f_baf.close()
