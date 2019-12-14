f = open('y.json')
f.readline()
f2 = open('prediction.csv')
truth = []
pred = []
while True:
	line = f.readline()
	if not line:
		break
	if len(line) < 10:
		continue
	truth.append(line.split(":")[1].rstrip('\n').rstrip(','))

while True:
	line = f2.readline()
	if not line:
		break
	pred.append(line.rstrip('\n'))

same = 0
for i in range(len(truth)):
	if truth[i] == pred[i]:
		same += 1

print(same / len(truth))

