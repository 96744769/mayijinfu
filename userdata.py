# dgideas@outlook.com

# https://tianchi.shuju.aliyun.com/getStart/information.htm?raceId=231573

dataByDate = {}

i = 0
with open('data/user_balance_table.csv', 'r') as f:
	for line in f:
		i += 1
		if i == 1:
			continue # ignore the first line
		if i%1024 == 0:
			print(str(i))
		csv = line.split(',')
		if csv[1] in dataByDate:
			dataByDate[csv[1]][0] += int(csv[4])
			dataByDate[csv[1]][1] += int(csv[8])
		else:
			dataByDate[csv[1]] = [int(csv[4]), int(csv[8])]
for date in dataByDate:
	print(date+'\t'+str(dataByDate[date][0])+'\t'+str(dataByDate[date][1]))