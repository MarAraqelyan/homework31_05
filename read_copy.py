f = open('reaganomics.txt')

sentence ="Federal income tax and payroll tax levels" 
lines = f.readlines()
for line in lines:
	if line.find(sentence) != -1:
		x = lines.index(line)

f.seek(0)
for i in range(x):
	text = f.readline()
	print(text)

f.close()
		


