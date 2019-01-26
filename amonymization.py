import sys
import argparse

arg = sys.argv
parser = argparse.ArgumentParser(description="anonimyzation of cna and snv data with saving relative order of mutation events alonge the each chromosome")
parser.add_argument('snv', help="file with SNV data")
parser.add_argument('cna', help="file with CNA data")
parser.add_argument('-s', '--step', default=1000, help="number of nucleotides between each mutation event")
#parser.add_argument('-z', '--threshold_zero', type=float, default=1, help="what fraction of samples with zero copy number does position can have to still be included this position in output")
#parser.add_argument('-r', '--reducing', type=int, default=1, help="keep only each N position and remove every other one")


########################

def relayRaceSerch(name, ch, pos, cna_data, start):
    current=start
    while name!=cna_data[current][0]:
        if current+1==len(cna_data):
        	return [-1, 0]
        current+=1
    while ch!=cna_data[current][1]:
        if current+1==len(cna_data):
            return [-1, 0]
        if cna_data[current][0]!=name:
            return [-1, current]
        current+=1
    while pos>=cna_data[current][2]:
        if pos<=cna_data[current][3]:
            return [current, current]
        if current+1==len(cna_data):
            return [-1, 0]
        if cna_data[current][0]!=name:
            return [-1, current]
        if cna_data[current][1]!=ch:
            return [-1, current]
        current+=1
    return [-1, current]
'''
arg=sys.argv
snv_col=[]
cna_col=[]
wey_input_SNV=arg[1]
wey_input_CNA=arg[2]

snv_col=[1,2,35,37]
cna_col=[1,2,3,4,5,6]
'''
###################################

def SNVextract(SNV_file_name):
	SNV_data=[]
	SNV_file_read=open(SNV_file_name, 'r')
	first_line=True
	for line in SNV_file_read:
		line.strip()
		if first_line:
			first_line=False
			continue
		if line=='':
			break
		pros_line=line.split('\t')
		sampl_names=pros_line[37].strip().strip('"').split(';')
		sampl_reads=pros_line[35].strip().strip('"').split(';')
		for i in range(len(sampl_names)):
			mut=[]
			mut.append(sampl_names[i])
			mut.append(pros_line[1].strip().strip('"').strip('chr').strip('ch').strip('Chr').strip('Ch').replace('X','23').replace('M','25'))
			mut.append(pros_line[2].strip().strip('"'))
			mut.append(sampl_reads[i].strip().strip('"').split(',')[0])
			mut.append(sampl_reads[i].strip().strip('"').split(',')[1])
			SNV_data.append(mut)

	SNV_file_read.close()
	for i in SNV_data:
		i[1]=int(i[1])
		i[2]=int(i[2])   
	SNV_data.sort(key=lambda x: [x[0],x[1],x[2]])
	print('------ SNV has been downloaded -----')
	return SNV_data
'''
#Take the SNV data
SNV_data=[]
SNV_file_read=open(wey_input_SNV, 'r')
first_line=True
for line in SNV_file_read:
    line.strip()
    if first_line:
        first_line=False
        continue
    if line=='':
        break
    pros_line=line.split('\t')
    sampl_names=pros_line[37].strip().strip('"').split(';')
    sampl_reads=pros_line[35].strip().strip('"').split(';')
    for i in range(len(sampl_names)):
    	mut=[]
    	mut.append(sampl_names[i])
    	mut.append(pros_line[1].strip().strip('"').strip('chr').strip('ch').strip('Chr').strip('Ch').replace('X','23').replace('M','25'))
    	mut.append(pros_line[2].strip().strip('"'))
    	mut.append(sampl_reads[i].strip().strip('"').split(',')[0])
    	mut.append(sampl_reads[i].strip().strip('"').split(',')[1])
    	SNV_data.append(mut)

SNV_file_read.close()
print('------ SNV has been downloaded -----')
print(SNV_data[3])
'''
##################################################

def CNAextract(CNA_file_name):
	CNA_file_read=open(CNA_file_name, 'r')    
	first_line=True
	CNA_data=[]
	for line in CNA_file_read:
		line.strip()
		if first_line:
			first_line=False
			continue
		if line=='':
			break
		pros_line=line.split('\t')
		alt=[]
		alt.append(pros_line[1].strip().strip('"'))
		alt.append(pros_line[2].strip().strip('"').strip('chr').strip('ch').strip('Chr').strip('Ch').replace('X','23').replace('M','25'))
		alt.append(pros_line[3].strip().strip('"'))
		alt.append(pros_line[4].strip().strip('"'))
		alt.append(pros_line[5].strip().strip('"'))
		alt.append(pros_line[6].strip().strip('"'))
		CNA_data.append(alt)
	CNA_file_read.close()
	for i in CNA_data:
		i[1]=int(i[1])
		i[2]=int(i[2])
		i[3]=int(i[3])    
	CNA_data.sort(key=lambda x: [x[0],x[1],x[2],x[3]])
	print('------ CNA has been downloaded -----')
	return CNA_data

'''
#Take the CNA data
CNA_file_read=open(wey_input_CNA, 'r')    
first_line=True
CNA_data=[]
for line in CNA_file_read:
    line.strip()
    if first_line:
        first_line=False
        continue
    if line=='':
        break
    pros_line=line.split('\t')
    alt=[]
    alt.append(pros_line[1].strip().strip('"'))
    alt.append(pros_line[2].strip().strip('"').strip('chr').strip('ch').strip('Chr').strip('Ch').replace('X','23').replace('M','25'))
    alt.append(pros_line[3].strip().strip('"'))
    alt.append(pros_line[4].strip().strip('"'))
    alt.append(pros_line[5].strip().strip('"'))
    alt.append(pros_line[6].strip().strip('"'))
    CNA_data.append(alt)
CNA_file_read.close()
print('------ CNA has been downloaded -----')
print(CNA_data[3])
'''
###################################

# Divided each CNA on two events

def CNA_dividing(CNA_data):
	num=0
	divided_CNV_data=[]
	for i in CNA_data:
		divided_CNV_data.append([i[0], i[1], i[2], i[4], i[5], num])
		num+=1
		divided_CNV_data.append([i[0], i[1], i[3], i[4], i[5], num])
		num+=1
	return divided_CNV_data
	
###################################

# Reasigned coordinate in CNA and SNV data

def reasigned_coordinates(SNV_data, divided_CNA_data, step=1000):
	chrom_changes={'22':'22', '23':'23', '24':'24', '25':'25', '26':'26', 'X':'X', 'M':'M'}
	for i in range(1, 22, 2):
		chrom_changes[str(i)]=str(i+1)
		chrom_changes[str(i+1)]=str(i)
	coordinate=0
	data=SNV_data+divided_CNA_data
	data.sort(key=lambda x: [x[0],x[1],x[2]])
	current_sample = data[0][0]
	current_chr = data[0][1]
	for event in range(len(data)):
		if current_sample != data[event][0] or current_chr!=data[event][1]:
			current_sample = data[event][0]
			current_chr = data[event][1]
			coordinate=0
		data[event][1]=chrom_changes[str(data[event][1])]
		coordinate+=step
		data[event][2]=coordinate
	reasigned_SNV_data=[]
	reasigned_CNA_data=[]
	for i in data:
		if len(i)==5:
			reasigned_SNV_data.append(i)
		elif len(i)==6:
			reasigned_CNA_data.append(i)
		else:
			print('error')
			print(i)
	return reasigned_SNV_data, reasigned_CNA_data
	
###################################

# Anti-divided CNA data

def setup_CNA_data(d_CNA_d):
	new_CNA_data=[]
	d_CNA_d.sort(key=lambda x: [x[5]])
	i=0
	while i < len(d_CNA_d):
		if d_CNA_d[i][0]!=d_CNA_d[i+1][0] or d_CNA_d[i][1]!=d_CNA_d[i+1][1]:
			print('error')
			print(d_CNA_d[i])
		if d_CNA_d[i][3]!=d_CNA_d[i+1][3] or d_CNA_d[i][4]!=d_CNA_d[i+1][4]:
			print('error')
			print(d_CNA_d[i])
		new_CNA_data.append([d_CNA_d[i][0],d_CNA_d[i][1],d_CNA_d[i][2],d_CNA_d[i+1][2],d_CNA_d[i][3],d_CNA_d[i][4]])
		i+=2
	return new_CNA_data
	
###################################


args = parser.parse_args()

SNV_data=SNVextract(args.snv)
CNA_data=CNAextract(args.cna)

divided_CNA_data=CNA_dividing(CNA_data)
reasigned_SNV_data, reasigned_CNA_data = reasigned_coordinates(SNV_data, divided_CNA_data, args.step)
new_CNA_data=setup_CNA_data(reasigned_CNA_data)

#CNA and SNV sorting

for i in reasigned_SNV_data:
    i[1]=int(i[1])
    i[2]=int(i[2])   
reasigned_SNV_data.sort(key=lambda x: [x[0],x[1],x[2]])
for i in new_CNA_data:
    i[1]=int(i[1])
    i[2]=int(i[2])
    i[3]=int(i[3])    
new_CNA_data.sort(key=lambda x: [x[0],x[1],x[2],x[3]])

# Write anonimyzed data

SNV_fw=open(args.snv.replace('.csv', '_anonimyzed.csv'), 'w')
SNV_fw.write('sample\tchr\tcoordinate\tDP\tAF\n')
for i in reasigned_SNV_data:
	SNV_fw.write(i[0]+'\t'+str(i[1])+'\t'+str(i[2])+'\t'+str(i[3]+i[4])+'\t'+str(i[4])+'\n')
SNV_fw.close()

CNA_fw=open(args.cna.replace('.csv', '_anonimyzed.csv'), 'w')
CNA_fw.write('sample\tchr\tstart\tend\tnMajor\tnMinor\n')
for i in new_CNA_data:
	CNA_fw.write(i[0]+'\t'+str(i[1])+'\t'+str(i[2])+'\t'+str(i[3])+'\t'+str(i[4])+'\t'+str(i[5])+'\n')
SNV_fw.close()

print('----- Completed -----')





###################################
'''
#CNA and SNV sorting
for i in SNV_data:
    i[1]=int(i[1])
    i[2]=int(i[2])   
SNV_data.sort(key=lambda x: [x[0],x[1],x[2]])

for i in CNA_data:
    i[1]=int(i[1])
    i[2]=int(i[2])
    i[3]=int(i[3])    
CNA_data.sort(key=lambda x: [x[0],x[1],x[2],x[3]])

#Tied up CNA and SNV
data=[]
step=[0, 0]
for i in SNV_data:
    data_line=[]
    data_line.append(i[0])
    data_line.append(i[1])
    data_line.append(i[2])
    data_line.append(int(i[3]))
    data_line.append(int(i[4]))
    data_line.append(2)
    step=relayRaceSerch(i[0],i[1],i[2],CNA_data,step[1])
    if step[0]==-1:
        data_line.append(0)
        data_line.append(2)        
    else:
        data_line.append(CNA_data[step[0]][5])
        data_line.append(CNA_data[step[0]][4])
    data.append(data_line)

#wey_out=wey_input_SNV.replace('csv', 'tsv')
wey_out=wey_input_SNV+'_CNA.tsv'
file_write=open(wey_out, 'w')
file_write.write('mutation_id\tref_counts\tvar_counts\tnormal_cn\tminor_cn\tmajor_cn\n')
for i in data:
    file_write.write(str(i[0])+':'+str(i[1])+':'+str(i[2])+'\t'+str(i[3])+'\t'+str(i[4])+'\t'+str(i[5])+'\t'+str(i[6])+'\t'+str(i[7])+'\n')       
file_write.close()
print('----- Completed -----')
'''
