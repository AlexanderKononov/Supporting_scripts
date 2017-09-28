import sys

arg=sys.argv
data=[]
#lable=True
f_cvf=open(arg[1], 'r')
f_baf=open(arg[1]+'baf.txt', 'w')
f_logR=open(arg[1]+'logR.txt', 'w')
for line in f_cvf:
	if line[0]=='#':
		continue
	#if lable:
	#	lable=False
	#	continue
	if line=='':
		break
	colm=line.strip().split('\t')
	colm[0]=colm[0].replace('chr','').replace('X', '23').replace('Y', '24').replace('M', '25')
	rg=colm[-1].strip().split(':')
	if len(rg)<=3:
		continue
	rb=rg[1].strip().split(',')
	#print(line)
	f_baf.write(str(colm[0])+'\t'+str(colm[1])+'\t'+str(int(rb[1]))+'\t'+str(rg[2])+'\n')
	f_logR.write(str(colm[0])+'\t'+str(colm[1])+'\t'+str(rg[2])+'\t'+'1'+'\n')
f_cvf.close()
f_baf.close()
f_logR.close()