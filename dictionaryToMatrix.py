def letterToNum(letter):
    return ord(letter) - ord('a')

#input is a dictionary representatin of a graph g and output is the matrix rep. for the graph
def dictionaryToMatrix(g):
    m = [[0]* len(g) for i in range(len(g))]
    for vertex, edges in g.items():
        vertex = letterToNum(vertex)
        for edge in edges:
            edge = letterToNum(edge)
            m[vertex][edge] = 1
    return m

g = {'a': ['b', 'c', 'd'], 'b': ['a', 'c'], 'c': ['a', 'b'], 'd': ['a']}
m = dictionaryToMatrix(g)
m
