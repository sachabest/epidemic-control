# geolocator.py - gets Lat/Lon (and optionally population)
# from a source network

import sys
import csv

node_map = dict()

def init(input_file):
	with open(input_file) as f:
		for line in f:
			splitted = line.split(' ')
			node = dict()
			if len(line) > 0:
				try:
					node['lat'] = float(splitted[4])
					node['lon'] = float(splitted[5])
					node['pop'] = long(splitted[2])
					node['cap'] = long(splitted[3])
					node_map[long(splitted[0])] = node
				except ValueError:
					print("Couldn't parse: " + line);
	print("Geolocated " + str(len(node_map)) + " nodes in database.");

edge_nodes = set()

def create_edge_filter(edge_list, output_file):
	with open(edge_list) as f:
		for line in f:
			splitted = line.split(' ')
			if len(line) > 1:
				try:
					node1 = long(splitted[0])
					node2 = long(splitted[1])
					edge_nodes.add(node1)
					edge_nodes.add(node2)
				except ValueError:
					print("Couldn't parse: " + line)
	with open(output_file, 'wb') as f:
		writer = csv.writer(f, delimiter=',')
		writer.writerow(['id', 'latitude', 'longitude', 'population', 'capacity'])
		for node in edge_nodes:
			if node < 1: continue
			print('locating ' + str(node))
			full_node = node_map[node]
			writer.writerow([node, full_node['lat'], full_node['lon'], full_node['pop'], full_node['cap']])

def main():
	if len(sys.argv) < 4:	
		print 'USAGE: geolocator.py source_data edge_list output_file'
	filename = sys.argv[1]
	edge_list = sys.argv[2]
	output_file = sys.argv[3]
	init(filename)
	create_edge_filter(edge_list, output_file)
if __name__ == '__main__':
	main()