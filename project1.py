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

def buildGraph(data, size, limit):
	g = nx.Graph()
	for index, line in enumerate(data):
		# print line
		words = line.split(' ')
		if index % 1000000 == 0:
			print index
		if len(words) > 2 and words[0].isdigit():
			node1 = int(words[0])
			node2 = int(words[2])
			if node1 < limit and node2 < limit:
				g.add_edge(node1, node2)
	return g

# keep track of what componenets we have already searched
# so that if our first try has less than 1000 nodes
# we can pick another and start again
components_searched = set()

# connected_componenets returns a the componenets in descending size order
# so we get random to make sure our entire group does not have the same subgraph
def get_components_random(graph, size):
	# print 'call get components random with ' + str(len(components_searched)) + ' components searched'
	num_lists = nx.number_connected_components(graph)
	lists = nx.connected_components(graph)
	i = 0;
	comp_list = list(lists)
	comp = comp_list[i]
	if len(components_searched) == 0:
		components_searched.add(i)
		return comp;
	# this will cause in a infinite loop with graphs less than 1000 nodes
	while comp is not None and i in components_searched and len(components_searched) < num_lists:
		i = i + 1;
		comp = comp_list[i]
		print comp
		# print "getting next component"
		components_searched.add(i);
	return comp

# generates a subgraph of a connected component in the larger graph
# by randomly selecting a component each time
def getSubgraph(graph, size, connectivity_ratio):
	nodes = set()
	lists = nx.connected_components(graph)
	for component in lists:
		if (len(nodes)) < size: 
			print 'component size' + str(len(components))
			nodes.update(component)
	# buffer size by 4 to handle connectivity problems
	#while len(nodes) <= connectivity_ratio * size:
		# print len(nodes)
		# print connectivity_ratio * size


		# comp = get_components_random(graph, size)
		# nodes.update(comp)
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
		print 'nodes: ' + str(nx.number_of_nodes(newGraph)) + ' required ' + str(size)
		if (nx.number_of_nodes(newGraph) >= size):
			# print nx.nodes(newGraph)
			return newGraph
	print 'did not generate enough nodes from connected components. Try a higher connectivity ratio'
	exit()

# main method
def main():
	if len(sys.argv) < 4:
		print 'Usage: project1.py filename nodecount connectivity_ratio explore_limit'
		exit()
	connectivity_ratio = float(sys.argv[3])
	nodeCount = int(sys.argv[2])
	if len(sys.argv) < 5:
		limit = 100 * nodeCount
	else:
		limit = int(sys.argv[4])
	g = buildGraph(readFile(sys.argv[1]), int(sys.argv[2]), limit)
	print 'graph loaded'
	subg = getSubgraph(g, nodeCount, connectivity_ratio)
	print 'subgraph loaded'
	bfsGraph = bfs(subg, nodeCount)
	print 'bfs finished'
	nx.write_edgelist(bfsGraph, 'out.txt')

if __name__ == '__main__':
	main()