# Aggregator
# Loads data into models and saves output metrics over time

import network
import networkx as  nx
import spreadingModel as model
import sys
import seedingStrategies
from operator import itemgetter

def simModel(model_name, net, output, b, d, g, e, th, ti):
	m = model.Models(net.getNodes(), b, d, g, e, th, ti)

	# call the funciton passed as a string
	getattr(m, model_name)()

	f = open(output + '_' + model_name, 'w')
	suscept_ratio = 0
	infect_ratio = 0
	vigilant_ratio = 0
	exposed_ratio = 0
	recovered_ratio = 0
	total_nodes = len(net.getNodes())

	for index, node in enumerate(m.nodes):
		nodestr = 'node : ' + node.id + ' : ' + node.getState()
		if node.getState() == 'INFECTED':
			infect_ratio += 1.0 / total_nodes
		elif node.getState() == 'SUSCEPTIBLE':
			suscept_ratio += 1.0 / total_nodes
		elif node.getState() == 'RECOVERED':
			recovered_ratio += 1.0 / total_nodes
		elif node.getState() == 'VIGILANT':
			vigilant_ratio += 1.0 / total_nodes
		elif node.getState() == 'EXPOSED':
			exposed_ratio += 1.0 / total_nodes
		#f.write(nodestr)
	
	print model_name + '\n'
	print 'infected ratio: ' + str(infect_ratio)
	print 'susceptible ratio: ' + str(suscept_ratio)
	print 'exposed ratio: ' + str(exposed_ratio)
	print 'vigilant ratio: ' + str(vigilant_ratio)
	print 'recovered ratio: ' + str(recovered_ratio) + '\n'

	f.close()

def main():
	if len(sys.argv) < 3:	
		print 'USAGE: aggregator.py input_file output_file'
	filename = sys.argv[1]
	output = sys.argv[2]
	net = network.Network()
	net.createNetwork(filename)
	net.createNodes(net.getGraph())
	sortedListByDegrees = sorted(net.getGraph().degree_iter(), key = itemgetter(1), reverse = True)
	theSeedingStrategy = seedingStrategies.SeedingStrategy(net.getGraph(), 5, net)
	net.updateNodes(theSeedingStrategy.kCoreDecomposition())
	simModel("SISmodel", net, output, 0.1, 0.3, 0.1, 0.3, 0.1, 1000)
	simModel('SIRmodel', net, output, 0.1, 0.3, 0.1, 0.3, 0.1, 1000)
if __name__ == '__main__':
	main()