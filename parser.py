import networkx as nx 
import Queue

def networkParser():
	G = nx.read_edgelist('tenmill_edges.txt', nodetype=int, create_using=nx.Graph())
	print ('building subgraph...')
	graph_list = nx.connected_component_subgraphs(G)
	i = 0
	subgraph = nx.Graph()
	for g in graph_list:
		i+=1
		source = nx.nodes(g)[0]
		#edges = nx.bfs_edges(g, source)
		edges = BFS_edges(g, source)
		for e1,e2 in edges:
			print (str(e1) + ' ' + str(e2))
			subgraph.add_edge(e1, e2)
			if nx.number_of_nodes(subgraph) >= 1000:
				break
		if nx.number_of_nodes(subgraph) >= 1000:
				break

	print ('Number of Nodes in Subgraph: ' + str(nx.number_of_nodes(subgraph)))
	print ('Number of Connected Components Used: ' + str(i))
	print ('Number of Connected Components in Subgraph: ' + str(nx.number_connected_components(subgraph)))


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
		for neighbor in curr.getNeighbors():
			if not (neighbor in visited):
				q.put(neighbor)
				visited.add(neighbor)
				output.append(curr, neighbor)
	return output

networkParser()