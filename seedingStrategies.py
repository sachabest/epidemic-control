import node
import network
import networkx as nx
from operator import itemgetter
#from numpy.linalg import eig

class SeedingStrategy:


	# self.net = net.getGraph() -- networkX
	# self.numberNodes = number of seed nodes
	# self.nodes = net.getNodes() -- our own node class
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
		#eigenvector_cent = nx.eigenvector_centrality(self.net, max_iter = 100, tol = .0005)
		#sortedListByEigenvectorCentrality = [(e, n) for n, e in eigenvector_cent.iteritems()]
		#sortedListByEigenvectorCentrality.sort()
		#sortedListByEigenvectorCentrality
		#sortedListByEigenvectorCentrality = sorted(nx.eigenvector_centrality(self.net, max_iter = 100, tol = .0005), key = itemgetter(1), reverse = False)
		#net_matrix = adj_matrix(self.net)
		eigenvectorCentralityDictionary = nx.eigenvector_centrality_numpy(self.net)
		sortedListByEigenvectorCentrality = sorted([(node, eigenvectorCentralityDictionary[node]) for node in eigenvectorCentralityDictionary], key = itemgetter(1), reverse = True)
		i = self.numberNodes
		while (i > 0):
			for node in self.nodes:
				if (self.nodes[node].getId() == sortedListByEigenvectorCentrality[0][0]):
					success = self.nodes[node].setState('INFECTED')
					if success:
						sortedListByEigenvectorCentrality.pop(0)
						break
			i -= 1
		return self.nodes

	def kCoreDecomposition(self):
		i = self.numberNodes
		for node in self.nodes:
			node.setCoreNumber(1)
		nodes_remaining = nx.k_core(self.net, 2)
		coreNumber = 2
		while (len(nodes_remaining) > 0):
			for node in nodes_remaining:
				currNode = self.nodes[node]
				currNode.setCoreNumber(coreNumber)
			coreNumber += 1
			nodes_remaining = nx.k_core(self.net, coreNumber)

		layers = dict()
		for node in self.nodes:
			key = node.getCoreNumber()
			if key in layers:
				layers[key].append(node)
			else:
				layers[key] = [node]

		sorted_layers = sorted(layers.keys(), reverse=True)
		for l in sorted_layers:
			if i == 0:
				break
			currNode = layers[l][0]
			success = currNode.setState('INFECTED')
			i -= 1
			
		return self.nodes

	def cascadingSize(self):
		i = self.numberNodes
		while (i > 0):
			
			i -= 1
		return self.nodes
