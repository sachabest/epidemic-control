import node
import network
import networkx as nx
from operator import itemgetter

class SeedingStrategy:


	# self.net = net.getGraph() -- networkX
	# self.numberNodes = number of seed nodes
	# self.nodes = net.getNodes() -- our own node class
	def __init__(self, net, numberNodes, nodes):
		self.net = net
		self.numberNodes = numberNodes
		self.nodes = nodes.values()

	def largestDegrees(self):
		sortedListByDegrees = sorted(self.net.degree_iter(), key = itemgetter(1), reverse = True)
		i = self.numberNodes
		while (i > 0):
			for node in self.nodes:
				if (node.getId() == sortedListByDegrees[0][0]):
					success = node.setState('INFECTED')
					if success:
						sortedListByDegrees.pop(0)
						break
			i -= 1
		return self.nodes

	def eigenvectorCentrality(self):
		sortedListByEigenvectorCentrality = sorted(nx.eigenvector_centrality(self.net), key = itemgetter(1), reverse = True)
		i = self.numberNodes
		while (i > 0):
			for node in self.nodes:
				if (node.getId() == sortedListByEigenvectorCentrality[0][0]):
					success = node.setState('INFECTED')
					if success:
						sortedListByDegrees.pop(0)
						break
			i -= 1
		return self.nodes

	def kCoreDecomposition(self):
		i = self.numberNodes
		while (i > 0):
			
			i -= 1
		return self.nodes

	def cascadingSize(self):
		i = self.numberNodes
		while (i > 0):
			
			i -= 1
		return self.nodes
