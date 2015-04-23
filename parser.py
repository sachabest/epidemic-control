import networkx as nx 
import Queue

def networkParser():
	G = nx.read_edgelist('output_part1/subgraph_edges_10.txt', nodetype=int, create_using=nx.Graph())
	print('Number of Nodes in Graph: ' + str(nx.number_of_nodes(G)))
	graph_list = nx.connected_component_subgraphs(G)
	i = 0
	nodes = set()
	subgraph = nx.Graph()
	for g in graph_list:
		i+=1
		#source = nx.nodes(g)[0]
		source = g.nodes()[0]
		#edges = nx.bfs_edges(g, source)
		edges = BFS_edges(g, source)
		for e1,e2 in edges:
			#print (str(e1) + ' ' + str(e2))
			nodes.add(e1)
			nodes.add(e2)
			subgraph.add_edge(e1, e2)
			if nx.number_of_nodes(subgraph) >= 1200:
				break
		if nx.number_of_nodes(subgraph) >= 1200:
				break
	print len(nodes)
	edgeFinder(nodes)
	print ('Number of Nodes in Subgraph: ' + str(nx.number_of_nodes(subgraph)))
	print ('Number of Connected Components Used: ' + str(i))
	print ('Number of Connected Components in Subgraph: ' + str(nx.number_connected_components(subgraph)))


def edgeFinder(nodes):
	with open('output_part1/subgraph_edges_10.txt') as f:
		for line in f:
			splitted = line.split(' ')
			if len(line) > 0:
				node1 = int(splitted[0])
				node2 = int(splitted[1])
				if (node1 in nodes) and (node2 in nodes):
					print (line)

def BFS_edges(graph, source):
	'''takes in a graph and a source node, of type Node
	returns a list of BFS edges'''
	q = Queue.Queue()
	parent_node = {}
	visited = set()
	output = []
	q.put(source)
	visited.add(source)
	while not q.empty():
		curr = q.get()
		for neighbor in graph.neighbors(curr):
			if not (neighbor in visited):
				q.put(neighbor)
				visited.add(neighbor)
				output.append((curr, neighbor))
	return output

networkParser()