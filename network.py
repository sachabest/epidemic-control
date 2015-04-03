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
            if n in nodes:
                node_n = nodes[n]
            else:
                node_n = node.Node(n)
                nodes[n] = node_n
            for n2 in g.neighbors(n):
                if n2 in nodes:
                    node_n2 = nodes[n2]
                else:
                    node_n2 = node.Node(n2)
                    nodes[n2] = node_n2
                node_n.addNeighbor(node_n2)
        self.theNodes = nodes

    def getGraph(self):
        return self.graph

    def getNodes(self):
        return self.theNodes

    def updateNodes(self, nodes):
        self.theNodes = nodes
