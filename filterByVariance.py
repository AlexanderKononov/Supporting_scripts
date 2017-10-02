import sys
import numpy as np

arg=sys.argv

#lable=True
#arg[1]='H002_B_Statisticfiltered.vcf'
f_cvf=open(arg[1], 'r')
f_bam=open(arg[1]+'_baf1000.txt', 'w')
f_cnv=open(arg[1]+'_cnv1000.txt', 'w')
step=1000
number_of_position=0
line='000'
#while number_of_position < 300:
while line!='':
    data=[]
    for j in range(step):
        line=f_cvf.readline()
        if line=='':
            break
        if line[0]=='#':
            continue
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
        number_of_position+=1
    
    if len(data)<=1:
        continue
    data=np.array(data)
    mean=data[:,3].mean()
    variance=data[:,3].var()
    down_lim=mean-(2*variance)
    up_lim=mean+(2*variance)
    for i in data:
        if i[3] > down_lim and i[3] < up_lim:
            f_bam.write((str(i[0])+'\t'+str(i[1])+'\t'+str(i[2]))+'\t'+str(i[3])+'\n')
            f_cnv.write((str(i[0])+'\t'+str(i[1])+'\t'+str(i[3]))+'\t'+'1'+'\n')

f_cvf.close()
f_cnv.close()
f_bam.close()
