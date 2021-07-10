# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 15:18:53 2021

@author: Zeel janani
"""
#karatsuba algorithm

X= int(input("ENter number 1: "))
Y= int(input("ENter number 2 :"))

def karatsuba(X,Y):
    #base condition
    if X<10 or Y<10:
        return X*Y
    m=max(len(str(X)),len(str(Y)))
    
    #converting odd to even num
    if m%2!=0:
        m-=1
    a,b=divmod(X,10**int(m/2))
    c,d=divmod(Y,10**int(m/2))
    ac = karatsuba(a,c)
    bd = karatsuba(b,d)
    ad_bc= karatsuba((a+b),(c+d))-ac-bd
    
    return ((ac*(10**m))+((ad_bc)*(10**int(m/2)))+bd) #karatsuba equation
    
s=karatsuba(X,Y)
print(s)