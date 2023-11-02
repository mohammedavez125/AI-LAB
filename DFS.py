# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 10:23:56 2023

@author: moham
"""
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 09:49:25 2023

@author: moham
"""
# DFS
from collections import defaultdict
class Graph:
    def __init__(self):
        self.Graph=defaultdict(list)
    def addEdge(self,u,v):
        self.Graph[u].append(v)
    def DFSUtil(self,v,visited):
        visited[v]=True
        print(v)
        for i in self.Graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)
    def DFS(self):
        v=len(self.Graph)
        visited=[False]*(v)
        for i in range(v):
            if (visited[i]==False):
                self.DFSUtil(i, visited)
g=Graph()
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,2)
g.addEdge(2,0)
g.addEdge(2,3)
g.addEdge(3,3)
print("Following is DFS (starting from vertex 1)")
g.DFS()
"""
Following is DFS (starting from vertex 1)
0
1
2
3
"""