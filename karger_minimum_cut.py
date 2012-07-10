# Karger minimum cut algorithm
# Returns the minimum number of cuts in a connected graph

import re
import random

def minimum_cut(graph):
    if len(graph) < 3:
        return graph
    # Find a random edge, first by finding random vertice
    vertice = random.choice(graph.keys())
    # Then by finding random connection
    connection = graph[vertice][random.randrange(0,len(graph[vertice]))]
    while (connection in graph.keys()) == False:
        connection = graph[vertice][random.randrange(0,len(graph[vertice]))]
    # Now merge edge into single vertex
    graph[vertice] += graph[connection]
    del graph[connection]
    # And remove self-loops
    graph[vertice] = filter (lambda a: a != vertice, graph[vertice])
    graph[vertice] = filter (lambda a: a != connection, graph[vertice])
    # And replace all references to connection with reference to vertice
    for key, value in graph.iteritems():
        graph[key] = [x if x != connection else vertice for x in value]
    minimum_cut(graph)
    return graph

if __name__=="__main__":
    # The following takes as input a file where the first column represents a vertex label
    # and the row tells all vertices that said vertex is adjacent to
    j = 0
    count_record = 40
    while j < 100: # This number of iterations may need to be increased
        file = open('edges.txt','r')
        p = re.compile(r'\b\d+\b')
        lines = file.readlines()
        interim = [line.strip() for line in lines if p.match(line)]
        vertices = [0]*len(interim)
        i = 0
        for row in interim:
            vertices[i] = re.findall(r'\b\d+\b', row)
            i += 1
        file.close()
        graph = {t[0]:t[1:] for t in vertices}
        minimum_cut(graph)
        count = 0
        for key, value in graph.iteritems():
            count += len(graph[key])
        count = count/2
        if count < count_record:
            count_record = count
            print "Total of",count,"connections in minimum cut"
            print graph
        j += 1
