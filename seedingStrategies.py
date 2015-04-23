import node
import network
import networkx as nx
import copy
from operator import itemgetter
#from numpy.linalg import eig

class SeedingStrategy:


	# self.net = net.getGraph() -- networkX
	# self.numberNodes = number of seed nodes
	# self.nodes = net.getNodes() -- our own node class
	def __init__(self, net, numberNodes, nodes, beta):
		self.net = net
		self.numberNodes = numberNodes
		self.nodes = nodes.getNodes()
		self.beta = beta

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
		# initialize all nodes to a k core number of 1
		for node in self.nodes:
			self.nodes[node].setCoreNumber(1)
		nodes_remaining = nx.k_core(self.net, 2)
		coreNumber = 2
		# keep removing nodes with k_core until the graph is empty
		while (len(nodes_remaining) > 0):
			for node in nodes_remaining:
				currNode = self.nodes[node]
				currNode.setCoreNumber(coreNumber)
			coreNumber += 1
			nodes_remaining = nx.k_core(self.net, coreNumber)

		# create a dict that maps an int to a list of all nodes with int=kCoreNumber
		layers = dict()
		for node in self.nodes:
			key = self.nodes[node].getCoreNumber()
			if key in layers:
				layers[key].append(node)
			else:
				layers[key] = [node]

		# start at the most central layer and choose one node from each layer
		# as we move farther from the core (which would be closer to the periphery)
		sorted_layers = sorted(layers.keys(), reverse=True)
		for l in sorted_layers:
			if i == 0:
				break
			currNode = layers[l][0]
			success = self.nodes[currNode].setState('INFECTED')
			i -= 1

		return self.nodes

	def cascadingSize(self):
		def findCascade(theInfectedNodesNotYetFlipped):
			numberInfectedNodes = 0
			while (len(theInfectedNodesNotYetFlipped) > 0):
				for node in theInfectedNodesNotYetFlipped:
					theInfectedNodesNotYetFlipped.remove(node)
					for neighbor in node.getNeighbors():
						if neighbor.getState() == 'SUSCEPTIBLE':
							success = neighbor.flipCoin(self.beta, 'INFECTED')
							if success:
								theInfectedNodesNotYetFlipped.append(neighbor)
								numberInfectedNodes += 1
			return numberInfectedNodes

		def reset():
			#print("resetting")
			for node in self.nodes:
				if self.nodes[node] not in startingInfectedNodes:
					self.nodes[node].setState('SUSCEPTIBLE')
				else:
					self.nodes[node].setState('INFECTED')
					#infectedNodesNotYetFlipped.append(self.nodes[node])
			#infectedNodesNotYetFlipped = startingInfectedNodes
			#print ("Not yet flipped:")
			#print (infectedNodesNotYetFlipped)
			#print ("^")

		def find_n_cascades(n, theInfectedNodesNotYetFlipped):
			totalNumberInfectedNodes = 0
			i = n
			while i > 0:
				totalNumberInfectedNodes += findCascade(theInfectedNodesNotYetFlipped)
				reset()
				i -= 1
			averageNumberInfectedNodes = totalNumberInfectedNodes / n
			return averageNumberInfectedNodes

		i = self.numberNodes
		self.largestDegrees()
		infectedNodesNotYetFlipped = []
		startingInfectedNodes = []
		for node in self.nodes:
			if self.nodes[node].getState() == 'INFECTED':
				infectedNodesNotYetFlipped.append(self.nodes[node])
				startingInfectedNodes.append(self.nodes[node])
		infectedNodesNotYetFlippedCopy = copy.copy(infectedNodesNotYetFlipped)
		averageNumberInfectedNodes = find_n_cascades(20, infectedNodesNotYetFlippedCopy)
		newlyAddedStartingInfectedNodes = copy.copy(startingInfectedNodes)
		while (len(newlyAddedStartingInfectedNodes) > 0):
			print ("iteration")
			for node in newlyAddedStartingInfectedNodes:
				print ("next iteration")
				print (newlyAddedStartingInfectedNodes)
				print (infectedNodesNotYetFlipped)
				print (startingInfectedNodes)
				node.setState('SUSCEPTIBLE')
				newlyAddedStartingInfectedNodes.remove(node)
				infectedNodesNotYetFlipped.remove(node)
				startingInfectedNodes.remove(node)
				maxAverageNumberInfectedNodesAmongNeighbors = -1
				maxNeighborNode = node
				for neighbor in node.getNeighbors():
					neighbor.setState('INFECTED')
					infectedNodesNotYetFlipped.append(neighbor)
					startingInfectedNodes.append(neighbor)
					infectedNodesNotYetFlippedCopy = copy.copy(infectedNodesNotYetFlipped)
					averageNumberInfectedNodesForNeighbor = find_n_cascades(20, infectedNodesNotYetFlippedCopy)
					startingInfectedNodes.remove(neighbor)
					infectedNodesNotYetFlipped.remove(neighbor)
					if averageNumberInfectedNodesForNeighbor > maxAverageNumberInfectedNodesAmongNeighbors:
						maxAverageNumberInfectedNodesAmongNeighbors = averageNumberInfectedNodesForNeighbor
						maxNeighborNode = neighbor
				if maxAverageNumberInfectedNodesAmongNeighbors > averageNumberInfectedNodes:
					startingInfectedNodes.append(maxNeighborNode)
					newlyAddedStartingInfectedNodes.append(maxNeighborNode)
					infectedNodesNotYetFlipped.append(maxNeighborNode)
				else:
					startingInfectedNodes.append(node)
		print ("Before Reset:")
		for node in self.nodes:
			if self.nodes[node].getState() == 'INFECTED':
					print ("new infected node:")
					print (node)
					print (self.nodes[node])
		reset()
		print ("After reset:")
		print ("Starting Infected Nodes:")
		print (startingInfectedNodes)
		for node in self.nodes:
			if self.nodes[node].getState() == 'INFECTED':
				print ("new infected node:")
				print (node)
				print (self.nodes[node])
		return self.nodes