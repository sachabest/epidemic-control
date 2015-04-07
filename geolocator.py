# geolocator.py - gets Lat/Lon (and optionally population)
# from a source network

import sys

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

def main():
	if len(sys.argv) < 3:	
		print 'USAGE: geolocator.py source_data to_modify'
	filename = sys.argv[1]
	output = sys.argv[2]
	init(filename)

if __name__ == '__main__':
	main()