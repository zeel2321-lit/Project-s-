# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 11:22:15 2021

@author: Zeel janani
"""


# A Dynamic Programming based Python 
# Program for 0-1 Knapsack problem
# Returns the maximum value that can 
# be put in a knapsack of capacity W
def knapSack(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]
  
    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:    #base condition
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w])
            else:           #overweight of the prodduct
                K[i][w] = K[i-1][w]
  
    return K[n][W]
  
# Driver program to test above function
val = [60, 100, 120]    #profit value for each product
wt = [10, 20, 30]       #weight for each product
W = 50                  #max of allowable weight
n = len(val)
print("Profit value is ",knapSack(W, wt, val, n))




#another approach
def Knapsaack(Val,Wt,w,N):
    if N==0 or w==0:
        return 0
    if(Wt[n-1]>w):
        return Knapsack(Val,Wt,w,N-1)
    else:
        return max(val[N-1]+Knapsaack(Val, Wt, w-Wt[N-1],N-1), Knapsaack(Val,Wt,w,N-1))
Val = [60, 100, 120]    #profit value for each product
Wt = [10, 20, 30]       #weight for each product
w = 50                  #max of allowable weight
N = len(val)
print("Profit value is ",Knapsaack(Val, Wt, w, N))