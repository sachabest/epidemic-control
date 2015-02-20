import networkx as nx
import sys
import node

class Network(): 

    def __init__(self):
        self.graph = nx.Graph()
        self.theNodes = dict()

    def createNetwork(self, filename):
        g = nx.Graph()
        f = open(filename, 'r')
        for line in f:
            l = line.split(' ')
            g.add_edge(l[0], l[1])
        self.graph = g

    def createNodes(self, g):
        nodes = dict()
        for n in g:
            node_n = node.Node(n)
            for n2 in g.neighbors(n):
                node_n.addNeighbor(n2)
            nodes[node_n] = n
        self.theNodes = nodes

    def getGraph(self):
        return self.graph

    def getNodes(self):
        return self.theNodes