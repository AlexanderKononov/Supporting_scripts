import sys
import numpy as np
import math

arg=sys.argv
data=[]
#lable=True
f_cvf=open(arg[1], 'r')
f_baf=open(arg[1]+'BAF2.txt', 'w')
step=10000
data=[]
lable_data=np.array([[0,0]])
line=f_cvf.readline()
while line!= '':
	line=f_cvf.readline()
	if line[0]=='#':
		continue
	for i in range(step):
		if line=='':
			break
		colm=line.strip().split('\t')
		colm[0]=colm[0].replace('chr','').replace('X', '23').replace('Y', '24').replace('M', '25')
		rg=colm[-1].strip().split(':')
		if len(rg)<=3:
			continue
		rb=rg[1].strip().split(',')
		if rb[1]==0:
			continue
		data.append(str(colm[0])+'\t'+str(colm[1])+'\t'+str(int(rb[1]))+'\t'+str(rg[2])+'\n')
		mdl=math.fabs((float(rb[1])/float(rg[2]))-0.5)
		
		lable_data=np.append(lable_data,[[int(i),float(mdl)]], axis=0)
		line=f_cvf.readline()
	print(lable_data[:,0])
	mean_baf=lable_data[:,1].mean()
	var_baf=np.var(lable_data[:,1])
	min_band=mean_baf-2*var_baf
	max_band=mean_baf+2*var_baf
	for i in lable_data:
		if i[1]>min_band and i[1]<max_band:
			f_baf.write(data[int(i[0]-1)])
	
f_cvf.close()
f_baf.close()
