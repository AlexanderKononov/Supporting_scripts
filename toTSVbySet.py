import sys

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

arg=sys.argv
snv_col=[]
cna_col=[]
wey_input_SNV=arg[1]
wey_input_CNA=arg[2]

snv_col=[1,2,35,37]
cna_col=[1,2,3,4,5,6]

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
