# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 17:45:14 2021

@author: Zeel Janani
"""

#rabin carp algorithm

text = "python"
pattern = "th"

X = len(text)
Y = len(pattern)
d = 256  #positional/radix base
flag = 0 

#find the sum for the pattern
sumP = 0
for i in range(Y):
    sumP = sumP + (ord(pattern[i]) * (d**(Y-i-1)))

#sum for the text
sumT = 0
for i in range(Y):
    sumT = sumT + (ord(text[i]) * (d**(Y-i-1)))
    
if (sumP == sumT):
    print("Pattern present in the text at " , i-Y+1)
    flag = 1

#Rolling hash function

for i in range(Y,X):
    sumT = (sumT - (ord(text[i-Y]) * (d**(Y-1))) ) * d + ord(text[i])
    
    if(sumP == sumT):
        print("Pattern present in the text at ", i-Y+1)
        flag = 1
        
if(flag == 0):
    print("Pattern is not present in the text")
        

