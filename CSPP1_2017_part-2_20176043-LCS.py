def longestSubstringFinder(string1, string2):
    answer = ""
    len1, len2 = len(string1), len(string2)
    for i in range(len1):
        for j in range(len2):
            lcs_temp=0
            match=''
            while ((i+lcs_temp < len1) and (j+lcs_temp<len2) and string1[i+lcs_temp] == string2[j+lcs_temp]):
                match += string2[j+lcs_temp]
                lcs_temp+=1
            if (len(match) > len(answer)):
                answer = match
    return answer

list1 = []
import os
for file in os.listdir():
	if file.endswith(".txt"):
		x = os.path.join(file)
		list1.append(x)
print(list1)

import re
words1=[]
for i in range(len(list1)):
	file = open(list1[i], 'r')
	text = file.read()
	file.close()
	text = re.sub('[^a-zA-Z0-9\ \']+', " ", text)
	text = text.replace(" ","")
	words = list(text.split())
	words1.append(words)

listfinal3 = []
for i in range(len(words1)):
	listfinal =[]
	for j in range(len(words1)):
		str1 = " ".join(str(x) for x in words1[i])
		length1 = len(str1)
		str2 = " ".join(str(x) for x in words1[j])
		length2 = len(str2)
		answer= longestSubstringFinder(str1,str2)
		totallength = length1 + length2
		#print(answer)
		#print(len(answer))
		finalanswer = ((len(answer) * 2) / totallength) * 100
		#print(finalanswer)
		print(list1[i],'vs',list1[j],'comparison is done and the answer is',finalanswer,'%')
		listfinal.append(finalanswer)
	listfinal3.append(listfinal)
for i in range(len(listfinal3)):
	print(listfinal3[i])