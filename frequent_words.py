import sys
import re
inputfile = ''
for line in sys.stdin:
    inputfile += line


word= {}
tempStr = ''
for i in inputfile:
    if re.search("[a-zA-Z]", i):
        tempStr += i
    else:
        if tempStr:
            if tempStr not in word:
                word[tempStr] = 1
            else:
                word[tempStr] += 1
            tempStr = ''

def bubble_sort(a):

    n = len(a)
    for i in range(n-1,0,-1):
        for j in range(i):
            if a[j][1] < a[j+1][1]:
                a[j], a[j+1] = a[j+1], a[j]
word_list = list(word.items())
bubble_sort(word_list)
k = 0
for i in word_list:
   print(i[0] +' ' + str(i[1]))
   k += 1
   if k == 20:
       break