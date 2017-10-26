import sys
import numpy as np
import matplotlib.pyplot as plt

arg=sys.argv
#weyCNA=raw_input('CNA file')
#weyCNA='/home/kononov/Desktop/test14/data/tu_cna.txt'
#weyCNA='testCNA.txt'

#weyBaf=raw_input('Baf file')
weySNV=arg[1]
#weyBaf='/home/kononov/Desktop/baf_viewer/H002_B1144_BAF2.txt'
#weyBaf='testBaf.txt'

#We introduce either the range through "-" or simply a number
#what_part=raw_input('What part of data you want to view? (in %)')
what_part='100'
print('-----Start-----')
part=[]
p=what_part.split('-')
if len(p)==2:
    part.append(int(p[0].strip()))
    part.append(int(p[1].strip()))
else:
    part.append(0)
    part.append(int(p[0].strip()))
print(part[0], part[1])    
#Choose a part of the data

dataSNV=[]
file_SNV =open(weySNV, 'r')
coint=0.0
size=sum(1 for l in open(weySNV, 'r'))
for line in file_SNV:
    coint+=1
    if part[0]<((coint/size)*100)<part[1]:
        sep_line=line.split()
        dataSNV.append(sep_line)
    else:
        continue
print('----downloaded----')

#cut data

dataSNVc=[]
i=0
while i<len(dataSNV):
    dataSNVc.append(dataSNV[i])
    i+=1
'''
i=0
curr_chr=dataCNAc[i][0]
addnum=0
delnum=0
while i<len(dataCNAc):
    if curr_chr!= dataCNAc[i][0]:
        addnum=addnum+dataCNAc[i-1][1]
        delnum=dataCNAc[i][1]
        curr_chr=dataCNAc[i][0]
    dataCNAc[i][1]=int(addnum)+int(dataCNAc[i][1])-int(delnum)
    i+=1
'''
i=0
curr_chr=dataSNVc[i][0]
addnum=0
delnum=0
while i<len(dataSNVc):
    if curr_chr!= dataSNVc[i][0]:
        addnum=addnum+dataSNVc[i-1][1]
        delnum=dataSNVc[i][1]
        curr_chr=dataSNVc[i][0]
    dataSNVc[i][1]=int(addnum)+int(dataSNVc[i][1])-int(delnum)
    i+=1

    
#data.pop(0)   #delite first string
    
plt.figure(figsize=(20, 8))

#Drawing cna
#ax=fig.add_axes([0.08,0.55,0.9,0.4])

#Drawing BAF
#ax=fig.add_axes([0.08,0.05,0.9,0.4])
#plt.subplot(212)
x_coin=0
x2=[]
y2=[]
for i in dataSNVc:
    alt=float(i[2])
    DP=float(i[3])
    ref=DP-float(i[2])
    if alt==0 or DP==0:
        continue
    #x2.append(int(i[1]))
    x2.append(x_coin)
    y2.append(alt/DP)
    x_coin+=1
plt.plot(x2,y2,'ko', markersize=1)
#plt.plot(x1, y1, linewidth=6, color='black')
plt.ylabel('SNV')
print('----SNV has been completed----')


plt.savefig('Fig', fmt='pdf')

#plt.show()

print('-----Completed------')
