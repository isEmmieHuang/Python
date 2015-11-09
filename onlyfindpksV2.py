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

#print(data)
top=[]
count=0
tmp2=[]
for i in range (len(data)):
    tmp=[]
    if data[i] ==0 and len(tmp2)==0:
        continue
    elif data[i] == 0 and len(tmp2)!=0:
        final=[]
        tmp4=[] #find time
        tmp3=[] #find Max value
        for j in tmp2:  #find MAX peak
            tmp3.append(j[0])
            tmp4.append(j[1])
            x=tmp3.index(max(tmp3))
        #final is Max of every tmp2     
        final.append(max(tmp3))
        final.append(tmp4[x])
        top.append(final)
        tmp2 = []
    else: #save 0-0 data
        tmp.append(data[i])
        tmp.append(i/10)
        tmp2.append(tmp)
print(top)

