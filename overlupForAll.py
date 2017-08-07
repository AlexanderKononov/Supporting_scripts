import sys

arg=sys.argv

nfile=len(arg)-1
coint=0
file_list=[]
line_list=[]
for i in range(nfile):
	file_list.append(open(arg[i+1],'r'))
fw=open('out.txt','w')
for f in file_list:
	line_list.append(f.readline().strip().split('\t'))
flg=0
while 0==0:
	current=[]
	brk=False
	#if line_list[i][0]=='3' and int(line_list[i][1])>198187632:
	#	flg=1
	for i in range(nfile-1):
		if brk:
			break
		if flg==1:
			print(i)
	
		while int(line_list[i][0])<int(line_list[i+1][0]):
			line_list[i]=file_list[i].readline().strip().split('\t')
			if len(line_list[i])<2:
				brk=True
				break
		while int(line_list[i][0])>int(line_list[i+1][0]):
			line_list[i+1]=file_list[i+1].readline().strip().split('\t')
			if len(line_list[i+1])<2:
				brk=True
				break

		if flg==1:
			print(str(line_list[i])+'---'+str(line_list[i+1]))
			print('------')
		while int(line_list[i][1])<int(line_list[i+1][1]):
			line_list[i]=file_list[i].readline().strip().split('\t')
			if len(line_list[i])<2:
				brk=True
				break
			if (line_list[i][0]!=line_list[i+1][0]):
				break
		if flg==1:
			print(str(line_list[i])+'---'+str(line_list[i+1]))
			
		while int(line_list[i][1])>int(line_list[i+1][1]):
			line_list[i+1]=file_list[i+1].readline().strip().split('\t')
			if len(line_list[i+1])<2:
				brk=True
				break
			if (line_list[i][0]!=line_list[i+1][0]):
				break
		if flg==1:
			print(str(line_list[i])+'---'+str(line_list[i+1]))
		current=line_list[i+1]

	# Write ontput
	coint+=1
	finde_pos=True
	for i in range(nfile):
		if line_list[i][0]!=current[0] or line_list[i][1]!=current[1]:
			finde_pos=False
	if flg==1:
			print(finde_pos)
	if finde_pos:
		fw.write(line_list[0][0]+'\t'+line_list[0][1])
		chrom1.add(line_list[0][0])
		for i in range(nfile):
			if flg==1:
				print(line_list[i])
			fw.write('\t'+line_list[i][2]+'\t'+line_list[i][3])
			line_list[i]=file_list[i].readline().strip().split('\t')
			if len(line_list[i])<2:
				brk=True
		fw.write('\n')

	# exet from cicle
	brk=False
	for i in range(nfile):
		if len(line_list[i])<2:
			brk=True
			break
	if brk:
		break


for i in file_list:
	i.close()
fw.close()
print(coint)