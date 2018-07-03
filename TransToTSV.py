import sys

def relayRaceSerch(ch, pos, cna_data, start):
    current=start
    #print(cna_data[current])
    while ch!=cna_data[current][0]:
        if current>=len(cna_data)-1:
            return [-1, current]
        current+=1
    while pos>=cna_data[current][1]:
        if pos<=cna_data[current][2]:
            return [current, current]
        if current>=len(cna_data)-1:
            return [-1, current]
        if cna_data[current][0]!=ch:
            return [-1, current]
        current+=1
    return [-1, current]

class Sep_cell:
	def __init__(self, targ_cell, sep):
		self.targ_cell=targ_cell
		self.sep=sep
		
def createTSVtoCurrentSample(sample_name, SNV_data, CNA_data, rate):
	#CNA and SNV sorting
	for i in SNV_data:
		i[0]=i[0].strip('chr').strip('ch').strip('Chr').strip('Ch').replace('X','23').replace('M','25')
		i[0]=int(i[0])
		i[1]=int(i[1])   
	SNV_data.sort(key=lambda x: [x[0],x[1]])

	for i in CNA_data:
		i[0]=i[0].strip('chr').strip('ch').strip('Chr').strip('Ch').replace('X','23').replace('M','25')
		i[0]=int(i[0])
		i[1]=int(i[1])
		i[2]=int(i[2])    
	CNA_data.sort(key=lambda x: [x[0],x[1],x[2]])
	
	#Tied up CNA and SNV
	data=[]
	step=[0, 0]
	for i in SNV_data:
		data_line=[]
		data_line.append(i[0])
		data_line.append(i[1])
		data_line.append(i[2])
		data_line.append(int(i[3]))
		data_line.append(2)
		step=relayRaceSerch(i[0],i[1],CNA_data,step[1])
		if step[0]==-1:
			data_line.append(0)
			data_line.append(2)        
		else:
			data_line.append(CNA_data[step[0]][4])
			data_line.append(CNA_data[step[0]][3])
		data.append(data_line) 


	#wey_out=wey_input_SNV.replace('csv', 'tsv')
	wey_out=sample_name+'.tsv'
	file_write=open(wey_out, 'w')
	file_write.write('mutation_id\tref_counts\tvar_counts\tnormal_cn\tminor_cn\tmajor_cn\n')
	
	current_time = 0
	for i in data:
		current_time += 1
		if (current_time % rate) != 0:
			continue
		
		nMin = int(float(i[5]))
		nMaj = int(float(i[6]))
		if (nMaj + nMin) == 0 : nMaj = 1
		file_write.write(str(i[0])+':'+str(i[1])+'\t'+str(i[2])+'\t'+str(i[3])+'\t'+str(i[4])+'\t'+ str(nMin)+'\t'+str(nMaj)+'\n')
		
		#file_write.write(str(i[0])+':'+str(i[1])+'\t'+str(i[2])+'\t'+str(i[3])+'\t'+str(i[4])+'\t'+ str("%.2f" % float(i[5]))+'\t'+str("%.2f" % float(i[6]))+'\n')
		#file_write.write(str(i[0])+':'+str(i[1])+'\t'+str(i[2])+'\t'+str(i[3])+'\t'+str(i[4])+'\t'+ str(int(float(i[5])))+'\t'+str(int(float(i[6])))+'\n')	
	file_write.close()
	

#Arguments prossesing
arg=sys.argv
snv_col=[]
cna_col=[]
print(arg)
wey_input_SNV=arg[1]
wey_input_CNA=arg[2]
print('Let\'s default run...' )
if '-h' in arg:
    print("help:\n usage: python TransToTSV.py [-h] -snv_f <SNV_data.csv> [column numbers from SNV_data] -cna_f <CNA_data> [column numbers from CNA_data] -d\n\n -d To start by default for HERCULES project data")
snv_col=[0,1,36]
cna_col=[1,2,3,4,8,9]

rate = 1
if len(arg) == 4: rate = int(arg[3])

#Take the SNV data
SNV_data=[]
sample_names = []
snv_col = []
SNV_file_read=open(wey_input_SNV, 'r')
line = SNV_file_read.readline()
heders = line.strip().split('\t')
for i in range(0, len(heders)):
	if heders[i].find('.AD') != -1:
		snv_col.append(i)
		sample_names.append(heders[i].strip().strip('"').strip('.AD'))
		
line = SNV_file_read.readline()
while line != '':
	pros_line = line.strip().split('\t')
	Na=False
	for check in pros_line:
		if check.strip().strip('"')=='NA':
			Na=True
	if Na:
		line = SNV_file_read.readline()
		continue
        
	for i in range(0, len(sample_names)):
		mut = []
		mut.append(sample_names[i])
		mut.append(pros_line[0].strip().strip('"').strip('chr').strip('ch').strip('Chr').strip('Ch').replace('X','23').replace('M','25'))
		mut.append(pros_line[1].strip().strip('"'))
		mut.append(pros_line[snv_col[i]].strip().split(',')[0].strip().strip('"'))
		mut.append(pros_line[snv_col[i]].strip().split(',')[1].strip().strip('"'))
		SNV_data.append(mut)
	line = SNV_file_read.readline()
'''	
first_line = True
for line in SNV_file_read:
    line.strip()
    if first_line:
        first_line=False
        continue
    if line=='':
        break
    pros_line=line.split('\t')
    mut=[]
    for i in snv_col:
    	if i==36:
    		cell=pros_line[i].strip('"').split(',')
    		for j in cell:
    			mut.append(j)
    		continue
    	mut.append(pros_line[i].strip('"'))
    Na=False
    for check in mut:
        if check=='NA':
            Na=True
    if Na:
        continue
    SNV_data.append(mut)
'''
SNV_file_read.close()    
print('------ SNV has been downloaded -----')

#Take the CNA data
CNA_file_read=open(wey_input_CNA, 'r')    
first_line=True
CNA_data=[]
cna_col = [1,2,3,4,8,9]
for line in CNA_file_read:
	line.strip()
	if first_line:
		first_line=False
		pline=line.split('\t')
		for i in range(0, len(pline)):
			if pline[i].strip().strip('"').find('samp') != -1: cna_col[0] = i
			if pline[i].strip().strip('"').find('chr') != -1: cna_col[1] = i
			if pline[i].strip().strip('"').find('start') != -1: cna_col[2] = i
			if pline[i].strip().strip('"').find('end') != -1: cna_col[3] = i
			if pline[i].strip().strip('"').find('Major') != -1: cna_col[4] = i
			if pline[i].strip().strip('"').find('Minor') != -1: cna_col[5] = i
		continue
	if line=='':
		break
	pline=line.split('\t')
	alt=[]
	for i in cna_col:
		alt.append(pline[i].strip().strip('"'))
	CNA_data.append(alt)
CNA_file_read.close()
print('------ CNA has been downloaded -----')


for sample_name in sample_names:
	current_sample_SNV = []
	current_sample_CNA = []
	for snv in SNV_data:
		if snv[0] == sample_name:
			current_sample_SNV.append([snv[1], snv[2], snv[3], snv[4]])
	for cna in CNA_data:
		if cna[0].find(sample_name) != -1 or sample_name.find(cna[0]) != -1:
			current_sample_CNA.append([cna[1], cna[2], cna[3], cna[4], cna[5]])
			
	createTSVtoCurrentSample(sample_name, current_sample_SNV, current_sample_CNA, rate)
	

print('----- Completed -----')
