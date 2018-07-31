import argparse
import sys

arg = sys.argv
parser = argparse.ArgumentParser(description="filtrating and sorting cna and snv from general tsv file")
parser.add_argument('input_file', help="general file (tsv) with SNV and CNA data")
parser.add_argument('-n', '--name_filter', default="", help="part of names of samples which should be included into analysis")
parser.add_argument('-z', '--threshold_zero', type=float, default=1, help="what fraction of samples with zero copy number does position can have to still be included this position in output")
parser.add_argument('-r', '--reducing', type=int, default=1, help="keep only each N position and remove every other one")


args = parser.parse_args()

f_r = open(args.input_file, 'r')
currentName = ''
data = {}
heder = f_r.readline()
line = f_r.readline()
while line != '':
	l = line.strip().split('\t')
	if l[0].find(args.name_filter) == -1:
		line = f_r.readline()
		continue
	name = l[0].strip().split(':')[0]
	if name != currentName:
		currentName = name
		data[name] = []
	l[0] = l[0].replace(name + ':', '')
	data[name].append(l)
	line = f_r.readline()
f_r.close()

print(str(len(data[currentName]))+' position was detected')

positions = []
for i in range(len(data[currentName])):
	zeros = 0
	for j in data.keys():
		if int(data[j][i][2]) == 0:
			zeros += 1
		if int(data[j][i][5]) == 0:
			zeros = len(data)
	if zeros <= len(data)*args.threshold_zero:
		positions.append(data[currentName][i][0])

print(str(len(positions))+' position was stayed after filtaration of zero copy number')

reduced_positions=[]
i = 0		
while i < len(positions):
	reduced_positions.append(positions[i])
	i += args.reducing
positions = reduced_positions

print(str(len(positions))+' position was stayed after reducing')	

for i in data.keys():
	f_w = open(i + '_sml.tsv', 'w')
	f_w.write(heder)
	for j in data[i]:
		if j[0] in positions:
			for l in j:
				f_w.write(l + '\t')
			f_w.write('\n')
	f_w.close()
