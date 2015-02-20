import networkx as nx
import sys
import node

class Network(): 

    def __init__(self):
        self.graph = nx.Graph()
        self.theNodes = dict()

    def createNetwork(filename):
        g = nx.Graph()
        f = open(filename)
        for line in f:
    	   l = line.split
    	   if not(l[0] in nodes):
    		  g.add_node(l[0])
    	   if not(l[1] in nodes):
    		  g.add_node(l[1])
    	   g.add_edge(l[0], l[1])
        self.graph = g

    def createNodes(g):
	    nodes = dict()
	    for n in g:
		    node = Node(n)
		    for n2 in g.neighbors(n):
			    node.addNeighbor(n2)
		    nodes.update(node, n)
        self.theNodes = nodes

    def getGraph():
        return self.graph

    def getNodes():
        return self.theNodes