import sys

def lion_in_desert(pos, CNA_data):
    cur_pos=len(CNA_data)/2
    up_bord=len(CNA_data)
    dowen_bord=0
    while 0==0:
        if cur_pos==dowen_bord:
            if CNA_data[dowen_bord][1]<=pos<=CNA_data[dowen_bord][2]:
                return CNA_data[dowen_bord]
            elif CNA_data[up_bord][1]<=pos<=CNA_data[up_bord][2]:
                return CNA_data[up_bord]
            else:
                return [0,0,2,0,2]
        elif CNA_data[cur_pos][0]>pos:
            up_bord=cur_pos
            cur_pos=dowen_bord+((up_bord-dowen_bord)/2)
        elif CNA_data[cur_pos][1]<pos:
            dowen_bord=cur_pos
            cur_pos=dowen_bord+((up_bord-dowen_bord)/2)
        else:
            return CNA_data[cur_pos]

arg=sys.argv
if len(arg)<3:
	wey_input_SNV=raw_input('input file SCV ')
	wey_input_CNA=raw_input('input file CNA (Segmentation) ')
else:
	wey_input_SNV=arg[1]
	wey_input_CNA=arg[2]
if '-h' in arg:
	print("help: ")
	break

if '-d' in arg:
	s_name=0
	s_ch=1
	s_pos=2
	s_RD=35
	c_name=0
	c_ch=2
	c_start=3
	c_end=4
	c_min=6
	c_maj=5
	c_ply=10

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
    deep=pros_line[35].strip('"').replace(',','.').split(';')
    mutation=[pros_line[0].strip('"')+':'+pros_line[1].strip('"')+':'+pros_line[2].strip('"'), int(float(deep[0])), int(float(deep[1])), 2, 0, 2]
    SNV_data.append(mutation)
SNV_file_read.close()    
print('------ SNV has been downloaded -----')

#Take the CNA data
CNA_file_read=open(wey_input_CNA, 'r')    
first_line=True
bibliography_dict={}
CNA_dict={}
for line in CNA_file_read:
    line.strip()
    if first_line:
        first_line=False
        continue
    if line=='':
        break
    pline=line.split('\t')
    for i in range(len(pline)):
        pline[i]=pline[i].strip().strip('"')
    if pline[0] not in bibliography_dict.keys():
        bibliography_dict[pline[0]]=pline[0].split('_')[0]
        CNA_dict[pline[0]]={}
        CNA_dict[pline[0]]['chr'+pline[2]]=[[int(pline[3]),int(pline[4]),int(pline[5]),int(pline[6]),pline[10]]]
    else:
        if 'chr'+pline[2] not in CNA_dict[pline[0]].keys():
            CNA_dict[pline[0]]['chr'+pline[2]]=[[int(pline[3]),int(pline[4]),int(pline[5]),int(pline[6]),pline[10]]]
        else:
            CNA_dict[pline[0]]['chr'+pline[2]].append([int(pline[3]),int(pline[4]),int(pline[5]),int(pline[6]),pline[10]])
CNA_file_read.close()
print('------ CNA has been downloaded -----')

#Tied up SNV and CNA data
for i in range(len(SNV_data)):
    tmpl=SNV_data[i][0].split(':')
    for key in bibliography_dict.keys():
        if key.find(tmpl[0])>=0:
            SNV_data[i][0]=key+':'+tmpl[1]+':'+tmpl[2]


#Find CNA data for each SNV
for i in range(len(SNV_data)):
    tmpl=SNV_data[i][0].split(':')
    pos=int(tmpl[2])
    CNA_line=lion_in_desert(pos, CNA_dict[tmpl[0]][tmpl[1]])
    SNV_data[i][4]=CNA_line[3]
    SNV_data[i][5]=CNA_line[2]
print('----- SNV and CNA is tied up -----')

#wey_out=wey_input_SNV.replace('csv', 'tsv')
wey_out='outTest.tsv'
file_write=open(wey_out, 'w')
file_write.write('mutation_id\tref_counts\tvar_counts\tnormal_cn\tminor_cn\tmajor_cn\n')
for i in SNV_data:
    file_write.write(str(i[0])+'\t'+str(i[1])+'\t'+str(i[2])+'\t'+str(i[3])+'\t'+str(i[4])+'\t'+str(i[5])+'\n')
        
file_write.close()
print('----- Completed -----')
