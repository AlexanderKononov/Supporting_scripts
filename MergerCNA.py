import sys 

arg=sys.argv

#a='H002_iAsc1_CL1_DNA1.bam.vcflogR.txt'
#b='H002_pOme1_CL12_DNA1.bam.vcflogR.txt'
doc1=open(arg[1],'r')
doc2=open(arg[2],'r')
doc1_w=open(arg[1]+'OL.txt','w')
doc2_w=open(arg[2]+'OL.txt','w')
i1=4
i2=4
coint=0
line1=doc1.readline()
lpr1=line1.strip().split('\t')
line2=doc2.readline()
lpr2=line2.strip().split('\t')
while 0==0 :
	if line1=='' or line2=='':
		break
#check the position and write overlapped position
	if lpr1[0]==lpr2[0]:
		if int(lpr1[1])<int(lpr2[1]):
			line1=doc1.readline()
			lpr1=line1.strip().split('\t')
			continue
		if int(lpr2[1])<int(lpr1[1]):
			line2=doc2.readline()
			lpr2=line2.strip().split('\t')
			continue
		coint+=1
		doc1_w.write(line1)
		doc2_w.write(line2)
		line1=doc1.readline()
		lpr1=line1.strip().split('\t')
		line2=doc2.readline()
		lpr2=line2.strip().split('\t')
		continue
	
#finding similar chromosome
	lpr1[0].replace('chr','').replace('X','23').replace('Y','24').replace('M','25')
	lpr2[0].replace('chr','').replace('X','23').replace('Y','24').replace('M','25')
	if int(lpr1[0])<int(lpr2[0]):
		line1=doc1.readline()
		lpr1=line1.strip().split('\t')
		continue
	if int(lpr2[0])<int(lpr1[0]):
		line2=doc2.readline()
		lpr2=line2.strip().split('\t')
		continue
	
	#if coint> 100:
	#	break
		
	if int(lpr1[0])<int(lpr2[0]):
		i1+=1
		continue
	if int(lpr2[0])<int(lpr1[0]):
		i2+=1
		continue
		
	#if coint> 100000:
	#	break
print(coint)
doc1.close()
doc1_w.close()
doc2.close()
doc2_w.close()
