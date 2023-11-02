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
        self.Graph[u].append((v))
        self.Graph[v].append((u))
    def dispg(self):
        print(self.Graph.items())
    def BFS(self,s,goal):
        visited=[False]*(len(self.Graph))
        frontier_q=[]
        frontier_q.append(s)
        visited[s]=True
        while frontier_q:
            s=frontier_q.pop(0)
            print(s,end=' ')
            if(s==goal):
                print("\n Goal found")
                return
            for i in self.Graph[s]:
                if visited[i]==False:
                    frontier_q.append(i)
                    visited[i]=True
                    print("\n Goal not found")
g=Graph()
g.addEdge(0, 1)
g.addEdge(0, 3)
g.addEdge(1, 2)
g.addEdge(2, 3)
g.addEdge(3,4)
g.addEdge(4,5)
g.addEdge(3,5)
g.dispg()
print("Following is BFS (starting from vertex 1)")
g.BFS(1,4)
"""
dict_items([(0, [1, 3]), (1, [0, 2]), (3, [0, 2, 4, 5]), (2, [1, 3]), (4, [3, 5]), (5, [4, 3])])
Following is BFS (starting from vertex 1)
1 
 Goal not found

 Goal not found
0 
 Goal not found
2 3 
 Goal not found

 Goal not found
4 
 Goal found
 """