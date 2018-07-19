import sys
import argparse

def getClusterList(cluster_file_name, threshold = 0):
	f_r = open(cluster_file_name, 'r')
	cluster_list = set()
	line = f_r.readline()
	line = f_r.readline()
	while line != '':
		l = line.split('\t')
		if int(l[2].strip()) > threshold:
			cluster_list.add(l[1].strip())
		line = f_r.readline()
	f_r.close()
	return cluster_list

def getMutationList(loci_data):
	mutation_list =[]
	for i in loci_data:
		mutation_list.append(i[0])
	mutation_list.pop(0)
	return mutation_list
		

def getData(file_name):
	f_r = open(file_name, 'r')
	data =[]
	line = f_r.readline().strip()
	while line != '':
		l = line.split('\t')
		for i in range(len(l)):
			l[i] = l[i].strip()
		data.append(l)
		line = f_r.readline().strip()
	f_r.close()
	for i in range(1, len(data)):
		data[i][1] = data[i][1].replace('sample', 'smpl')
	return data

def getReadData(read_file_list):
	f_r = open(read_file_list[0], 'r')
	l = ['sample_id']
	for i in f_r.readline().strip().split('\t'):
		l.append(i.strip()) 
	data = [l]
	f_r.close()
	for file_name in read_file_list:
		f_r = open(file_name, 'r')
		line = f_r.readline()
		line = f_r.readline()
		while line != '':
			l = line.split('\t')
			line_for_add = [file_name.split('/')[-1][0:-4]]
			for i in range(len(l)):
				line_for_add.append(l[i].strip())
			data.append(line_for_add)
			line = f_r.readline().strip()
		f_r.close()
	return data

def filtrationByList(data, suite_list, key_word = 'clust'):
	l = data[0]
	for i in range(len(l)):
		if l[i].find(key_word) != -1:
			colomn_for_filtration = i
			break
	out_data = [data[0]]
	for i in data:	
		if  i[colomn_for_filtration].strip() in suite_list:
			out_data.append(i)
	return out_data


def writeMutToCluster(loci_data):
	f_w = open('mut-to-cluster.tsv', 'w')
	f_w.write('mutationID\tclusterID\n')
	current_mutation = ''
	for i in range(1,len(loci_data)):
		if current_mutation == loci_data[i][0]: continue
		current_mutation = loci_data[i][0]
		f_w.write(loci_data[i][0] + '\t' + loci_data[i][2] +'\n')		
	f_w.close()
	
def writeClusterEstimates(loci_data):
	f_w = open('clusterEstimates.tsv', 'w')
	f_w.write('sampleID\tmutationID\tcellularity\tsd\n')
	for i in range(1,len(loci_data)):
		f_w.write(loci_data[i][1] + '\t' + loci_data[i][0] + '\t' + loci_data[i][3] + '\t' + loci_data[i][4] + '\n')		
	f_w.close()

def writeMutRead(read_data):
	f_w = open('mut-read.tsv', 'w')
	f_w.write('sampleID\tmutationID\treferenceReads\tvariantReads\tcopyNumber\n')
	for i in range(1,len(read_data)):
		cN = str(int(read_data[i][5]) + int(read_data[i][6]))
		f_w.write(read_data[i][0] + '\t' + read_data[i][1] + '\t' + read_data[i][2] + '\t' + read_data[i][3] + '\t' + cN + '\n')		
	f_w.close()


#arg = sys.argv
parser = argparse.ArgumentParser(description = "Transfer output data tables of PyClone to input files for SCHOSM. Take cluster loci files and original tsv files of samples.")
parser.add_argument("cluster", help = "PyClone output file with cluster information")
parser.add_argument("loci", help = "PyClone output file with loci information")
parser.add_argument("sample_tsv_files", nargs = '*', help = "PyClone input files which used for PyClone analysis and harbor information about mutation. It is tsv files per sample")
parser.add_argument("-t", "--threshold", default = 0, type = int, help = "Clustr with size less then this threshold are filtered out") 


args = parser.parse_args()


cluster_list = getClusterList(args.cluster, threshold = args.threshold)
#print(cluster_list)
loci_data = getData(args.loci)
loci_data = filtrationByList(loci_data, cluster_list)
writeMutToCluster(loci_data)
writeClusterEstimates(loci_data)
print('---Detect essential clusters: ' + str(len(cluster_list)))
mutation_list = getMutationList(loci_data)
#arg.pop(0)
#arg.pop(0)
#arg.pop(0)
read_data = getReadData(args.sample_tsv_files)
read_data = filtrationByList(read_data, mutation_list, key_word = 'mutat')
writeMutRead(read_data)
print('---Considered mutations: ' + str(len(mutation_list)))
