"""
Analyzes duplicate dump files and calculates the minimum file
set for invalidating
"""
import sys


def buildGraph(lines):
    
    graph = {}
    i = 0
    while i < len(lines):
        lumi = lines[i].split()[1]
        f1 = lines[i+1]
        f2 = lines[i+2]
        #create edge f1 -> f2
        if f1 not in graph:
            graph[f1] = {}
        if f2 not in graph[f1]:
            graph[f1][f2] = 0
        graph[f1][f2] += 1
        #create edge f2 -> f1       
        if f2 not in graph:
            graph[f2] = {}
        if f1 not in graph[f2]:
            graph[f2][f1] = 0
        graph[f2][f1] += 1
        i += 3
    return graph

def getSumDegree(graph, v):
    return sum( e for v2, e in graph[v].items())

def hasEdges(graph):
    for v in graph.values():
        if v:
            return True
    return False

def deleteMaxDegreeFirst(graph):
    files = []
    print len(graph)
    #quadratic first
    while hasEdges(graph):
        maxv = None
        maxd = 0
        #get vertex with highest degree
        for v in graph:
            d = getSumDegree(graph,v)
            if d > maxd:
                maxd = d
                maxv = v
        #remove maxv from all its adjacent vertices
        for v in graph[maxv]:
            del graph[v][maxv]
        #remove maxv entry
        del graph[maxv]    
        files.append(maxv)
    print len(files), len(graph)
    return files

def main():
    lines = [l.strip() for l in open(sys.argv[1])]
    graph = buildGraph(lines)
    files = deleteMaxDegreeFirst(graph)
    for f in files:
        print f

if __name__ == '__main__':
    main()

