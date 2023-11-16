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
        self.Graph = defaultdict(list)
        self.num_vertices = 0
    def addEdge(self, u, v):
        self.num_vertices = max(self.num_vertices, u, v)
        self.Graph[u].append(v)
    def DFSUtil(self, v, visited):
        visited[v] = True
        print(v)
        for i in self.Graph[v]:
            if not visited[i]:
                self.DFSUtil(i, visited)
    def DFS(self):
        visited = [False] * (self.num_vertices + 1)  
        for i in range(self.num_vertices + 1): 
            if not visited[i]:
                self.DFSUtil(i, visited)
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(2, 3)
g.addEdge(3, 4)
g.addEdge(3, 5)
g.addEdge(4, 2)
print("Following is DFS (starting from vertex 0)")
g.DFS()

"""
Following is DFS (starting from vertex 1)
0
1
2
3
"""