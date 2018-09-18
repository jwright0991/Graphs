import string, math
import  collections
from itertools import combinations
from string import ascii_lowercase as lower
#words is a list of words that are allowed to be used in the word ladder
#start is initial word
#end is the word that we are changing start to
#returns a list of the words in the word ladder
#if the word ladder is not possible, return none
s = "cat"
e = "dog"
def getWordsFromFile(fileName):
    wordFile = open(fileName, 'r')
    wordList = []
    for line in wordFile:
        wordList.append(line[0:len(line)-1])
    wordFile.close()
    return wordList

def word_ladder(start,end):
    words = getWordsFromFile('google-10000-english.txt')
    g = buildGraph(start,end,words)
    bfsTree = BFS(g,start)
    if bfsTree[end][0] == math.inf:
        return "The there is no word ladder for the two chosen words"
    return getPathFromStartToEnd(bfsTree,end)
    
    
def wordsWithSameLength(start,words):
    return [word for word in words if len(word) == len(start)]     
#w1 and w2 are words of the same length
#returns true if they differ by one letter, false otherwise
def difByOneLetter(w1,w2):
    countDiff = 0
    i = 0
    while countDiff < 2 and i < len(w1):
        if w1[i] != w2[i]:
            countDiff +=1
        i+=1
    if(countDiff <= 1):
        return True
    else:
        return False
def buildGraph(start,end,words):
    wordList = wordsWithSameLength(start,words)
    wordList.append(start)
    wordList.append(end)
    g = {}
    for word in wordList:
        g[word] = []
    for i in range(len(wordList)):
       for j in range(len(wordList)):
            if difByOneLetter(wordList[i],wordList[j]) and wordList[i] != wordList[j]:
                      g[wordList[i]].append(wordList[j])

    return g
#runs BFS on undirected graph g starting at vertex s
#the function returns a dictionary where the keys are the names of the vertices and the values
#are lists of length two hwere the first value of the list is the distance from the key to s, and
#the second value is the parent of key in the BFS tree. 
def BFS(g, s):    
    dist = {word : [math.inf, None] for word in g}
    q = collections.deque()
    dist[s][0] = 0
    q.append(s)
    while q:
        v1 = q.popleft()
        for v2 in g[v1]:
            if dist[v2][0] == math.inf:
                dist[v2][0] = dist[v1][0] + 1
                dist[v2][1] = v1
                q.append(v2)
    return dist       
def getPathFromStartToEnd(bfsTree,end):
    path = [end]
    endVertex = bfsTree[end]
    pathLength = endVertex[0]
    parent = endVertex[1]
    while pathLength > 0:
        path.insert(0,parent)
        nextVertex = bfsTree[parent]
        pathLength = nextVertex[0]
        parent = nextVertex[1]
    return path


       
 
