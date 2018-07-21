from sklearn import metrics
import sys

def takeClast(nameFile):
	mut_dict = {}
	print(nameFile)
	f_r = open(nameFile, 'r')
	line = f_r.readline()
	line = f_r.readline()
	while line != '':
		l = line.strip().split('\t')
		cluster = ''
		for i in range(1, len(l)):
			cluster = cluster + str(l[i].strip().strip('"'))
		mut_dict[l[0].strip().strip('"')] = cluster
		line = f_r.readline()
	f_r.close()
	return mut_dict
	
arg = sys.argv

true_dict = takeClast(arg[1])
pred_dict = takeClast(arg[2])

mut = set()
for i in true_dict.keys():
	for j in pred_dict.keys():
		if i == j: mut.add(i)


true_list = []
pred_list = []
for i in mut:
	true_list.append(true_dict[i])
	pred_list.append(pred_dict[i])
print(len(true_list))
print(len(pred_list))


print(metrics.homogeneity_score(true_list, pred_list))
print(metrics.completeness_score(true_list, pred_list))
print(metrics.v_measure_score(true_list, pred_list))

