from __future__ import print_function

with open('subgraph_edge_list.txt') as f:
	for line in f:
		if len(line.strip()) == 0:
			continue
		else:
			print (line, end = "")