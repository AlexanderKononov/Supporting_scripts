
# coding: utf-8

# In[41]:

import sys
arg=sys.argv
fst=0
name_list=[]
f_w=open(arg[1],'r')
lable=f_w.readline().strip().split('\t')

#create list of files
for col in range(len(lable)):
    if lable[col].strip('"')=='FS':
        fst=col+1
        continue
    if fst!=0:
        name_list.append(lable[col].strip('"').strip('.AD'))

#clean list of files
i=0
while i<len(name_list):
    if name_list[i].find('.DP')!=-1:
        name_list.pop(i)
        continue
    i+=1

#create files
file_list=[]
for i in name_list:
    file_list.append(open(i+'.snv.txt','w'))


for line in f_w:
    lp=line.strip().split('\t')
    i=fst
    j=0
    while i<len(lp):
        if lp[i+1]=='NA':
            i+=2
            j+=1
            continue
        chrom=lp[0].strip('"').strip('chr').replace('X','23').replace('Y','24').replace('M','25')
	if chrom!='24' and chrom!='25':
		AD=lp[i].strip('"').split(',')
        	file_list[j].write(chrom+'\t'+lp[1].strip('"')+'\t'+AD[1]+'\t'+lp[i+1]+'\n')
        j+=1
        i+=2

#close files
for i in file_list:
    i.close()
    


# In[ ]:



