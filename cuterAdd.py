import sys
arg=sys.argv

fr=open(arg[1],'r')
fw=open('out.txt','w')
chr_list=[]
for i in range(24):
	chr_list.append(str(i))
print(chr_list)
for line in fr:
	lnsep=line.strip().split('\t')
	if lnsep[0] in chr_list:
		fw.write(line)
fr.close()
fw.close()
