import networkx as nx 

def networkParser():
	G = nx.read_edgelist('tenmill_edges.txt', nodetype=int, create_using=nx.Graph())
	print ('building subgraph...')
	graph_list = nx.connected_component_subgraphs(G)
	i = 0
	subgraph = nx.Graph()
	for g in graph_list:
		i+=1
		source = nx.nodes(g)[0]
		edges = nx.bfs_edges(g, source)
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

networkParser()