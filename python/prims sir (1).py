# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 14:25:03 2021

@author: Zeel Janani
"""

def createadjmatrix(V,G):
    adjmatrix = [[0 for i in range(V)]for j in range(V)]
    
    for i in range(0,len(G)):
        adjmatrix[G[i][0]][G[i][1]] = G[i][2]
        adjmatrix[G[i][1]][G[i][0]] = G[i][2]
        
    return adjmatrix
                                   
                                   

def prims(V,G):
    adjmatrix=createadjmatrix(V,G)
    vertex = 0
    
    edges = []    #creating the list of all the edges
    visited = []
    MST = []
    minEdge = [None,None,float("inf")]  #seeing if the edge selected is min or not
    
    while len(MST) != V-1:
        visited.append(vertex)
        
        for r in range(0,V):
            if adjmatrix[vertex][r] != 0:
                edges.append([vertex,r,adjmatrix[vertex][r]])
                
        for e in range(len(edges)):
            if edges[e][2] < minEdge[2] and edges[e][1] not in visited:
                minEdge = edges[e]
                 
                
        MST.append(minEdge)
        edges.remove(minEdge)
        
        vertex = minEdge[1]
        minEdge = [None,None,float('inf')]
    return MST

   
a,b,c,d,e,f = 0,1,2,3,4,5
graph = [[a,b,2],[a,c,3],[b,d,3],[b,c,5],[b,e,4],[c,e,4],[d,e,2],[d,f,3],[e,f,5]]

print(prims(6,graph))

