import sys

arg = sys.argv
f_r = open(arg[1], 'r')
f_w = open(arg[1], 'r')
currentName = ''
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
		f_w.close()
		f_w = open(name + '.tsv', 'w')
		f_w.write(heder)
	line = line.replace(name + ':', '')
	f_w.write(line)
	line = f_r.readline()

f_w.close()
f_r.close()
