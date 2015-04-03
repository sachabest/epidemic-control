import node
import network
import networkx as nx
from operator import itemgetter

class SeedingStrategy:

	def __init__(self, net, numberNodes, nodes):
		self.net = net
		self.numberNodes = numberNodes
		self.nodes = nodes.getNodes()

	def largestDegrees(self):
		sortedListByDegrees = sorted(self.net.degree_iter(), key = itemgetter(1), reverse = True)
		i = self.numberNodes
		while (i > 0):
			for node in self.nodes:
				if (self.nodes[node].getId() == sortedListByDegrees[0][0]):
					success = self.nodes[node].setState('INFECTED')
					if success:
						sortedListByDegrees.pop(0)
						break
			i -= 1
		return self.nodes

	def eigenvectorCentrality(self):
		sortedListByEigenvectorCentrality = sorted(nx.eigenvector_centrality(self.net, max_iter = 10000, tol = .1), key = itemgetter(1), reverse = True)
		i = self.numberNodes
		while (i > 0):
			for node in self.nodes:
				if (self.nodes[node].getId() == sortedListByEigenvectorCentrality[0][0]):
					success = self.nodes[node].setState = 'INFECTED'
					if success:
						sortedListByEigenvectorCentrality.pop(0)
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
