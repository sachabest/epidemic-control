import networkx as nx
import sys
import zipfile
import random

# load in graph using filennx zip loader

def readFile(filename):
	if not 'zip' in filename:
		return open(filename)
	zf = zipfile.ZipFile(filename, 'r')
	# this is unecessary for now, only one input file
	# print zf.infolist()
	for file in zf.infolist():
		data = zf.open(file, 'r')
	return data

def buildGraph(data):
	g = nx.Graph()
	lines = data.readlines()
	for line in lines:
		# print line
		words = line.split(' ')
		if len(words) > 2 and words[0].isdigit():
			node1 = int(words[0])
			node2 = int(words[2])
			g.add_edge(node1, node2)
	return g

# keep track of what componenets we have already searched
# so that if our first try has less than 1000 nodes
# we can pick another and start again
components_searched = set()

# connected_componenets returns a the componenets in descending size order
# so we get random to make sure our entire group does not have the same subgraph
def get_components_random(graph, size):
	num_lists = nx.number_connected_components(graph)
	lists = nx.connected_components(graph)
	i = int(random.randrange(num_lists))
	comp_list = list(lists)
	comp = comp_list[i]
	if len(components_searched) == 0:
		components_searched.add(i)
	# this will cause in a infinite loop with graphs less than 1000 nodes
	while comp is not None and i in components_searched and len(components_searched) < num_lists:
		i = random.randrange(num_lists)
		comp = comp_list[i]
		# print "getting next component"
		components_searched.add(i);
	return comp

# generates a subgraph of a connected component in the larger graph
# by randomly selecting a component each time
def getSubgraph(graph, size):
	nodes = set()
	
	while len(nodes) <= size:
		comp = get_components_random(graph, size)
		nodes.update(comp)
	print nodes
	return nx.subgraph(graph, nodes)

# keep track of random nodes started for bfs
nodes_searched = set()

# runs a bfs on the graph to grab nodes out of it
def bfs(graph, size):
	newGraph = nx.Graph()
	edges = set()
	node_count = len(nx.nodes(graph))
	# random-restart bfs untill enough nodes are in the set
	i = int(random.randrange(node_count))
	while len(edges) < size:
		edges.update(nx.bfs_edges(graph, nx.nodes(graph)[i], False))
		nodes_searched.add(i)
		# generate new random number
		while i in nodes_searched:
			i = int(random.randrange(node_count))

	print edges
	for edge in edges:
		newGraph.add_edge(edge[0], edge[1])
		if (nx.number_of_nodes(newGraph) > size):
			print nx.nodes(newGraph)
			return newGraph

# main method
def main():
	if len(sys.argv) < 3:
		print 'Usage: project1.py filename nodecount'
		exit()

	g = buildGraph(readFile(sys.argv[1]))
	nodeCount = int(sys.argv[2])
	subg = getSubgraph(g, nodeCount)
	bfsGraph = bfs(subg, nodeCount)
	print nx.nodes(bfsGraph)
	nx.write_edgelist(bfsGraph, 'out.txt')

if __name__ == '__main__':
	main()