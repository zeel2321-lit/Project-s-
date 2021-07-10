# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 00:19:30 2021

@author: Zeel Janani
"""

def matrixchainmultiplication(d,n):
    m=[[0 for i in range(n)]for j in range(n)]
    for i in range(1,n):
        m[i][i]=0  #principle diagpnal
    for D in range(1,n-1):   #difference matrix
        for i in range(1,n-D):
            j=i+D
            m[i][j]=10000
            for k in range(i,j):
                q=m[i][k]+m[k+1][j]+d[i-1]*d[k]*d[j]
                if(q<m[i][j]):
                   m[i][j]=q
    return m[1][n-1]
        
    d=[5,4,6,2,7]
size=len(d)
m=matrixchainmultiplication(d,size)
print(m)
