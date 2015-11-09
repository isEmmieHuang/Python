#--coding: UTF-8 --
#--coding: cp950 --
#測試資料輸入到 list 中

import sys
import os
import itertools
import math
import numpy as np
import itertools as it
import random
import time
import matplotlib.pyplot as plt
from pylab import *
#name = sys.argv[1]

name = input('file name:')#test-data name
data = []
f = open(name,'r')  	    #read data

with open(name) as file:
    for line in file:
        nums = [ num if len(num) > 3 else int(num) for num in line.split()]
        data.extend(nums)
f.close()
#輸入結束

##波峰
top=[]
count=0
tmp2=[]
for i in range (len(data)):
    tmp=[]
    if data[i] <= 1 and len(tmp2)==0:
        continue
    elif data[i] <= 1 and len(tmp2)!=0:
        final=[]
        tmp4=[] #find time
        tmp3=[] #find Max value
        for j in tmp2:  #find MAX peak
            tmp3.append(j[0])
            tmp4.append(j[1])
            x=tmp3.index(max(tmp3))
        #final is Max of every tmp2
        if max(tmp3) >2:
            final.append(max(tmp3))
            final.append(tmp4[x])
            top.append(final)
        tmp2 = []
    else: #save 0-0 data
        tmp.append(data[i])
        tmp.append(i/10)
        tmp2.append(tmp)

print(top,len(top))


"""
##波峰
top = []  #存波峰和時間
#temp = [max(data[i],data[i+1]) for i in range(len(data)-1)]

z=0 #Calculate the number of repetitions
for i in range(0,len(data)): #find pks(波峰) sava in temp[]
    temp = []
    if(0<=i<=len(data)-2):  #avoid index out of range
        if (data[i] == data[i+1]):
            z=z+1
            continue
            
        if(data[i] > data[i+1] and data[i] > data[i-z-1]):
            temp.append(data[i])
            temp.append((i/20))
            top.append(temp)
            #print("zz",z,data[i])
            #z=0
            continue
    elif(i==len(data)):
        continue
    z=0
print(top,len(top))
"""

##週期
tmppks = []
period = 0
count = 0
period2 = 0
freq =[] #countk/minute = frequency
'''

for j in range(len(top)):
    if(0<=j<=len(top)-2):
        if(top[j+1][1] == top[j][1]):
            continue

        if(top[j+1][1] > top[j][1]):
            period = top[j+1][1] - top[j][1]
        freq.append(1/period)
        #print(top[j+1][1],top[j][1],freq)
print(len(freq))
'''

for j in range(len(top)):
    if(0<=j<=len(top)-3):
        if(top[j+1][1] == top[j][1]):
            continue

        if(top[j+1][1] > top[j][1]):
            period = (top[j+2][1] - top[j][1])/2
            freq.append(1/period)
print(freq)
print(len(freq))
'''
############################# 還要再改！！！！
for j in range(len(top)):
    if(top[j][0] >= 10): 
        tmppks.append(top[j][1])

for k in range(len(tmppks)):
    if(0 <= k <= len(tmppks)-2):
        period = tmppks[k+1] - tmppks[k]
        
        if(period > 2):
            countk = countk+1
        
        if(period > 4):
            countk = countk+2
            
    #print(period)
print(countk,k)
freq = countk #要記得除以測試時間
string = 'freq. = ' + str(freq) #string裡存頻率
print(string) 
#print(tmppks)

'''
string = 'freq. = ' + str(freq) #string裡存頻率

## plot
x = np.arange(len(data))
y = data

x2 = []
y2 = []
for pks in top:
    x2.append(pks[1]*10)
    y2.append(pks[0])

plt.figure(figsize = ( 30 , 5 ))

x3 = np.arange(len(top)-2)
y3 = freq

'''
plt.subplot(211)
plt.title(name + '\t ' + string)
plt.xticks([0,1200,2400,3600,4800,6000])
plt.plot(x,y,color="gray",label="$pulmonary$")
plt.ylabel("Amplitude")
plt.grid()
plt.legend(loc = 'upper right')
'''
plt.subplot(211) 
plt.xticks([0,1200,2400,3600,4800,6000])
plt.plot(x,y,color="gray",label="$pulmonary$")
plt.plot(x2,y2,"ro",label="$pks$")
plt.xlim ( 0 , len(data))
plt.xlabel("Time (ms)")
plt.ylabel("Amplitude")
plt.grid()
plt.legend(loc = 'lower right')

plt.subplot(212)
plt.xticks(range(0,len(top),10))
plt.plot(x3,y3,color="gray",label="$frequency$")
plt.plot(x3,y3,"ro")
plt.legend(loc = 'lower right')
plt.xlim ( 0 , len(top))
plt.ylim ( 0, max(freq))
plt.grid()
plt.show()

