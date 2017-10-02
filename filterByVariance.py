import sys

arg=sys.argv

#lable=True
f_cvf=open(arg[1], 'r')
f_bam=open(arg[1]+'_baf11.txt', 'w')
f_cnv=open(arg[1]+'_cnv11.txt', 'w')
step=100
line='000'
while line!='':
	data=[]
	for j in range(step):
		line=f_cvf.readline()
		if line=='':
			break
		if line[0]=='#':
			continue
		#if lable:
		#	lable=False
		#	continue
		colm=line.strip().split('\t')
		if colm[6]!='PASS':
			continue
		colm[0]=colm[0].replace('chr','').replace('X', '23').replace('Y', '24').replace('M', '25')
		rg=colm[-1].strip().split(':')
		if len(rg)<=3:
			continue
		rb=rg[1].strip().split(',')
		#print(line)
		data.append([int(colm[0]),int(colm[1]),int(rb[1]),int(rg[2])])
	if len(data)<=1:
		continue
	x=0
	for i in data:
		x+=i[3]
	x=x/len(data)
	SD=0
	for i in data:
		SD+=(i[3]**2 - x**2)
	SD=SD/(len(data)-1)
	down_lim=x-(1*SD)
	up_lim=x+(1*SD)
	for i in data:
		if i[3] > down_lim and i[3] < up_lim:
			f_bam.write((str(i[0])+'\t'+str(i[1])+'\t'+str(i[2]))+'\t'+str(i[3])+'\n')
			f_cnv.write((str(i[0])+'\t'+str(i[1])+'\t'+str(i[3]))+'\t'+'1'+'\n')

f_cvf.close()
f_cnv.close()
f_bam.close()
