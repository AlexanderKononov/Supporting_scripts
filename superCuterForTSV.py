import sys

arg = sys.argv
rate = 1
if len(arg) == 4:
	rate = float(arg[3])
f_r = open(arg[1], 'r')
currentName = ''
data = {}
heder = f_r.readline()
line = f_r.readline()
while line != '':
	l = line.strip().split('\t')
	if l[0].find(arg[2]) == -1:
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

positions = []
for i in range(len(data[currentName])):
	zeros = 0
	for j in data.keys():
		if int(data[j][i][2]) == 0:
			zeros += 1
		if int(data[j][i][5]) == 0:
			zeros = len(data)
	if zeros < len(data)/rate:
		positions.append(data[currentName][i][0])

for i in data.keys():
	f_w = open(i + '_sml.tsv', 'w')
	f_w.write(heder)
	for j in data[i]:
		if j[0] in positions:
			for l in j:
				f_w.write(l + '\t')
			f_w.write('\n')
	f_w.close()
