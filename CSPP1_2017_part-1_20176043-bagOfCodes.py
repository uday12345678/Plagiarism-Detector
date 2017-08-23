def dictionary(l1,l2):
	d1 = {}
	for i in l1:
		if i in d1:
			d1[i] += 1
		else:
			d1[i] = 1
	d2 = {}
	for j in l2:
		if j in d2:
			d2[j] += 1
		else:
			d2[j] = 1
	return d1,d2

def numerator(d1,d2):
	tsum = 0
	for i in d1:
		for j in d2:
			if i == j:
				tsum = tsum + d1[i] * d2[j]
	return(tsum)

def denominator(d1,d2):
	sum1 = 0
	for i in d1:
		sum1 = sum1 + d1[i]**2
		squareroot1 = sum1**(1/2)
	sum2 = 0
	for i in d2:
		sum2 = sum2 + d2[i]**2
		squareroot2 = sum2**(1/2)
	total = squareroot1 * squareroot2
	return(total)
def euclidianpercentage(sum,total):
	answer = (tsum/total) * 100
	return(answer)
list1 = []
import os
for file in os.listdir():
	if file.endswith(".txt"):
		#print(os.path.join(file))
		x = os.path.join(file)
		list1.append(x)
		#print(len(x))
print(list1)

import re
words1=[]
for i in range(len(list1)):
	file = open(list1[i], 'r')
	text = file.read().lower()
	file.close()
	text = re.sub('[^a-z\ \']+', " ", text)
	words = list(text.split()) 
	# print(words)
	words1.append(words)
print (words1)
count = 0
listfinal3 = []
#print(words1[0][34])
for i in range(len(words1)):
	listfinal =[]
	for j in range(len(words1)):
		d1,d2= dictionary(words1[i],words1[j])
		tsum = numerator(d1,d2)
		total = denominator(d1,d2)
		answer = euclidianpercentage(tsum,total)
		count = count + 1
		print(count)
		#print(i,i+1)
		#print(list1[i],'vs',list1[i+1])
		print(list1[i],'vs',list1[j],'comparison is done and the answer is',answer,'%')
		listfinal.append(answer)
	listfinal3.append(listfinal)
for i in range(len(listfinal3)):
	print(listfinal3[i])
listfinal4 = []
for i in range(len(listfinal)):
	if listfinal[i] > 35:
		listfinal4.append(listfinal[i])
print(listfinal4)