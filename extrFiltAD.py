import sys
import numpy as np
import math

arg=sys.argv
data=[]
#lable=True
f_cvf=open(arg[1], 'r')
f_baf=open(arg[1]+'BAF_f0.1.txt', 'w')
step=1000
delcoin=0
line=f_cvf.readline()
while line!= '':
	if line[0]=='#':
		line=f_cvf.readline()
		continue
	data=[]
	lable_data=np.array([(0,0,0)], dtype=[('pos', int),('baf', float),('lvl', int)])
	for i in range(step):
		if line=='':
			break
		colm=line.strip().split('\t')
		colm[0]=colm[0].replace('chr','').replace('X', '23').replace('Y', '24').replace('M', '25')
		rg=colm[-1].strip().split(':')
		if len(rg)<=3:
			line=f_cvf.readline()
			continue
		rb=rg[1].strip().split(',')
		if rg[2]=='0':
			line=f_cvf.readline()
			continue
		data.append(str(colm[0])+'\t'+str(colm[1])+'\t'+str(int(rb[1]))+'\t'+str(rg[2])+'\n')
		
		#mdl=math.fabs((float(rb[1])/float(rg[2]))-0.5)
		baf=float(rb[1])/float(rg[2])
		lvl=baf//0.1

		lable_data=np.insert(lable_data,-1,(len(data)-1,float(baf), lvl), axis=0)
		line=f_cvf.readline()
	#print(lable_data[:,0])
	lable_data=np.sort(lable_data, order='lvl')
	#print(lable_data)
	memb_lvl=0
	curr_lvl=0
	del_list_lvl=[]
	for i in lable_data:
		if i[2]!=curr_lvl:
			if memb_lvl<=10:
				del_list_lvl.append(curr_lvl)
			curr_lvl=i[2]
			memb_lvl=0
			continue
		memb_lvl+=1
		
	lable_data=np.sort(lable_data, order='pos')
	
	'''	
	while i <=len(lable_data):
		if lable_data[i][2] in del_list_lvl:
			lable_data=np.delete(lable_data, i, 0)
			continue
		i+=1
	'''	
		
	for i in lable_data:
			if i[2] in del_list_lvl:
				continue
			f_baf.write(data[int(i[0])])	
	'''
	up_data=np.array([[0,0]])
	down_data=np.array([[0,0]])
	for i in lable_data:
		if i[1]>=0.5:
			up_data=np.append(up_data, [[i[0],i[1]]], axis=0)
	mean_baf=lable_data[:,1].mean()
	var_baf=np.var(lable_data[:,1])
	mean_up=up_data[:,1].mean()
	var_up=np.var(up_data[:,1])
	min_mead_band=mean_baf-2*var_baf
	max_mead_band=mean_baf+2*var_baf
	min_up_band=mean_up-2*var_up
	max_up_band=mean_up+2*var_up
	coint_up=0
	coint_mead=0
	for i in lable_data:
		if i[1]>min_mead_band and i[1]<max_mead_band:
			coint_mead+=1
		if i[1]>min_up_band and i[1]<max_up_band:
			coint_up+=1
	#print(len(data))
	#print(len(lable_data))
	if coint_mead>=coint_up:
		for i in lable_data:
			if i[1]>min_mead_band and i[1]<max_mead_band:
				f_baf.write(data[int(i[0])])
	else:
		for i in lable_data:
			if (i[1]>min_up_band and i[1]<max_up_band) or (i[1]<(1-min_up_band) and i[1]>(1-max_up_band)):
				f_baf.write(data[int(i[0])])
	'''
f_cvf.close()
f_baf.close()
