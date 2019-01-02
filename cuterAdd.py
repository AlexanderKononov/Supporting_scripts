import sys
arg=sys.argv

fr1 = open(arg[1],'r')
fr2 = open(arg[2],'r')
fw = open('Z_true2.csv','w')
var_data = []
z_data = []
line1 = fr1.readline()
line2 = fr2.readline()
fw.write(line2)
line1 = fr1.readline()
line2 = fr2.readline()
while line1 != '':
	lp1 = line1.strip().split('\t')
	lp2 = line2.strip().split('\t')[0].split(':')
	var_data.append([lp1[0], lp1[1], line1])
	z_data.append([lp2[0], lp2[1], line2])
	line1 = fr1.readline()
	line2 = fr2.readline()
fr1.close()
fr2.close()
for i in var_data:
	for j in z_data:
		if i[0] == j[0] and i[1] == j[1]:
			fw.write(j[2])
			break
fw.close()
