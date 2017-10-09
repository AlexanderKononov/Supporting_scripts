import sys 

arg=sys.argv

fil_r=open(arg[1], 'r')
fil_w=open(arg[1]+'CHRs.bed', 'w')
line = '000'
resol=10000
chr_lis=['chrX']
for i in range(23):
	chr_lis.append('chr'+str(i))
while line!='':
	line = fil_r.readline()
	line_p=line.strip().split('\t')
	if line_p[0]!='@SQ':
		continue
	if len(line_p[1])>10:
		continue
	chrom=line_p[1].strip().split(':')
	if chrom[1][-1]=='Y' or chrom[1][-1]=='M':
		continue
	if chrom[1] in chr_lis:
		LN=line_p[2].strip().split(':')
		l=1+resol
		while l<int(LN[1]):
			fil_w.write(chrom[1]+'\t'+str(l-resol)+'\t'+str(l)+'\n')
			l+=resol
fil_r.close()
fil_w.close()
