def getUnmarkedKeys(g):
    marked = {}
    for key in g.keys():
        marked.update({key:0})
    return marked

def markVertex(marked,vertex):
    marked.pop(vertex)
    marked.update({vertex:1})
    
def isUnmarked(marked,vertex):
    return not marked.get(vertex)

def allMarked(marked):
    allMarked = True
    for key in marked:
        if marked.get(key)==0:
            allMarked = False
    return allMarked
    
def BFS(g):
    #create a dictionary with the keys all set to unmarked
    marked = getUnmarkedKeys(g)
    #remove the starting vertex arbitrarily
    startingVertex = g.popitem()
    #add the starting vertex back to the graph
    g.update({startingVertex[0]:startingVertex[1]})
    
    q = []
    #mark V as visited and enqueue it 
    markVertex(marked,startingVertex[0])
    q.append(startingVertex[0])
    
    while len(q) > 0:
        #remove the head of the q
        vertex = q.pop(0)
        
        #get the list of adjacent vertices
        adjacentVertices = g.get(vertex)
        
        for adjVert in adjacentVertices:
            if isUnmarked(marked,adjVert):
                q.append(adjVert)
                markVertex(marked,adjVert)
    return allMarked(marked)

def hasEvenDegree(vertex):
    return len(vertex) % 2 == 0
def allVertHaveEvenDegree(g):
    for key in g:
        values = g.get(key)
        if hasEvenDegree(g.get(key)) != True:
            return False
    return True
def isEulerianDictionary(g):
    isEulerian = False
    if allVertHaveEvenDegree(g):
        isEulerian = BFS(g)
    return isEulerian
graph = {'a':['b','c','d','e'],'b':['a','c','d','e'],'c':['a','b','d','e'],'d':['a','b','c','e'],'e':['a','b','c','d']}
print(isEulerianDictionary(graph))


   
