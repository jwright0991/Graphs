from string import ascii_lowercase as lower
import math
import collections
def getUnmarkedKeys(g):
    marked = {x:0 for x in lower[:len(g)]}
    return marked

def markAllVisited(bfsTree, marked):
    for v in bfsTree:
       if not bfsTree[v][0] == math.inf:
           marked[v] = 1
def markVertex(marked,vertex):
    marked[vertex] = 1
    return

def isUnmarked(marked,vertex):
    return not marked[vertex]

def allMarked(marked):
    allMarked = True
    for key in marked:
        if marked[key]== math.inf:
            allMarked = False
    return allMarked
    
def BFS(g, start):
    #create a dictionary with the keys all set to unmarked
    marked = {x:0 for x in lower[:len(g)]}
    #remove the starting vertex arbitrarily
    q = deque()
    #mark V as visited and enqueue it 
    marked[start] = 1
    q.append(start)
    while q:
        #remove the head of the q
        v1 = q.popleft()
        for v2 in g[v1]:
            if not marked[v2] ==1:
                q.append(v2)
                marked[v2] == 1
    return allMarked(marked)

def BFS2(g, start):
   result = {x:[math.inf, None] for x in lower[:len(g)]}
   q = collections.deque()
   result[start][0] = 0
   q.append(start)
   while q:
        v1 = q.popleft()
        for v2 in g[v1]:
            if result[v2][0] == math.inf:
                result[v2][0] = result[v1][0]+1
                result[v2][1] = v1
                q.append(v2)
   #append and popleft
   return result
#return True is g is connected, else False:
def isConnected(g):
    bfsTree = BFS2(g,lower[0])
    isConnected = True
    for vertex in bfsTree:
        if bfsTree[vertex][0] == math.inf:
            isConnected == false
    return isConnected
#return the number of connected components in a graph
def numCC(g):
   count = 0
   nodes = set(g)
   while nodes:
       bfsTree = BFS2(g,nodes.pop())
       for v in bfsTree:
           if bfsTree[v][0] < math.inf:
               nodes.discard(v)
       count +=1

   return count
g = {'a': ['b', 'c', 'd'],
     'b': ['a', 'c'],
     'c': ['a', 'b'],
     'd': ['a'],
     'e': ['f'],
     'f': ['e'],
     'g': [],
     
     }             
                    
        
    
    
    
