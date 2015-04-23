'''assume I have a list of Nodes

variables include: 
-beta (trasmission probability over an edge if susceptible)
-delta (healing probability once infected)
-gamma (immunization-loss probability once recovered or vigilant)
-epsilon (virus-maturation probability once exposed)
-theta (direct-immunization probability when susceptible)

SIS Model
for each time step:
	for each node:
		if susceptible, look at neighbors
			for each neighbor
				if neighbor is infected, flipCoin on beta with potentialState='INFECTED'
				else do nothing
				break when the current node we're looking at gets infected
		if infected 
			flipCoin on delta with potentialState='SUSCEPTIBLE'
'''

import csv
import json

class Models():
	def __init__(self, nodes):
		
		self.nodes = nodes.values()
		# I made all these up, feel free to change
		self.beta = 0.3
		self.delta = 0.3
		self.gamma = 0.1
		self.epsilon = 0.3
		self.theta = 0.1
		self.time = 1000 #default used in the paper

	def __init__(self, nodes, b, d, g, e, th, ti):
		self.nodes = nodes.values()
		self.beta = b
		self.delta = d
		self.gamma = g
		self.epsilon = e
		self.theta = th
		self.time = ti

	def SISmodel(self):
		node_dynamic_map = dict()
		with open('states.csv','wb') as csvfile:
			# downsampled to 20%
			for i in xrange(self.time):
				#each of these nodes should be of type Node class in node.py
				for node in self.nodes:
					if node.getState() == 'SUSCEPTIBLE':
						#print 'changing neighbors of' + str(node.id)
						for neighbor in node.getNeighbors():
							if neighbor.getState() == 'INFECTED':
								success = node.flipCoin(self.beta, 'INFECTED')
								#stop looping through the neighbors if the node we're looking at is infected
								if success:
									break
					elif node.getState() == 'INFECTED':
						node.flipCoin(self.delta, 'SUSCEPTIBLE')
					# sample: [1.0, 2.0,a]; 
					# downsampled to 20%
					if i % 5 == 0:
						state_int = 0
						if node.getState() == 'INFECTED':
							state_int = 1
						dynamic_string = '[' + str(i) + ', ' + str(i+1) + ', ' +  str(state_int) + ']';
						if node.getId() in node_dynamic_map:
							node_dynamic_map[node.getId()].append(dynamic_string)
						else:
							node_dynamic_map[node.getId()] = [dynamic_string]
			fields = ['Id', "State"];
			csvwriter = csv.DictWriter(csvfile, fieldnames=fields)
			for nodeKey in node_dynamic_map:
				textInner = '<'
				for timestep in node_dynamic_map[nodeKey]: 
					textInner += timestep
					textInner += '; '
				textInner = textInner[:len(textInner) - 2]
				textInner += '>'
				csvwriter.writerow({'Id': nodeKey, 'State': textInner})


	'''
	SIR Model
	for each time step:
		for each node:
			if susceptible, look at neighbors
				for each neighbor
					if neighbor is infected, flipCoin on beta with potentialState='INFECTED'
					else do nothing
					break when the current node we're looking at gets infected
			if infected 
				flipCoin on delta with potentialState='RECOVERED'
			if recovered, do nothing
	'''

	def SIRmodel(self):
		for i in xrange(self.time):
			for node in self.nodes:
				if node.getState() == 'SUSCEPTIBLE':
					for neighbor in node.getNeighbors():
						if neighbor.getState() == 'INFECTED':
							success = node.flipCoin(self.beta, 'INFECTED')
							#stop looping through the neighbors if the node we're looking at is infected
							if success:
								break
				elif node.getState() == 'INFECTED':
					node.flipCoin(self.delta, 'RECOVERED')


	'''
	SIRS Model
	for each time step:
		for each node:
			if susceptible, look at neighbors
				for each neighbor
					if neighbor is infected, flipCoin on beta with potentialState='INFECTED'
					else do nothing
					break when the current node we're looking at gets infected
			if infected 
				flipCoin on delta with potentialState='RECOVERED'
			if recovered
				flipCoin on gamma with potentialState='SUSCEPTIBLE'
	'''

	#closest to ebola
	def SIRSmodel(self):
		node_dynamic_map = dict()
		for node in self.nodes:
			state_int = 0
			if (long(node.getId().strip())) in node_dynamic_map:
				node_dynamic_map[long(node.getId().strip())].append(state_int)
			else:
				node_dynamic_map[long(node.getId().strip())] = [state_int]
		for i in xrange(self.time):
			for node in self.nodes:
				if node.getState() == 'SUSCEPTIBLE':
					for neighbor in node.getNeighbors():
						if neighbor.getState() == 'INFECTED':
							success = node.flipCoin(self.beta, 'INFECTED')
							print('infecting node: ' + node.getId())
							#stop looping through the neighbors if the node we're looking at is infected
							if success:
								break
				elif node.getState() == 'INFECTED':
					node.flipCoin(self.delta, 'RECOVERED')
				elif node.getState() == 'RECOVERED':
					node.flipCoin(self.gamma, 'SUSCEPTIBLE')
				# sample: [1.0, 2.0,a]; 
				state_int = 0;
				if node.getState() == 'INFECTED':
					state_int = 1
				elif node.getState() == 'RECOVERED':
					state_int = 2
				if (long(node.getId().strip())) in node_dynamic_map:
					node_dynamic_map[long(node.getId().strip())].append(state_int)
				else:
					node_dynamic_map[long(node.getId().strip())] = [state_int]
		json_str = json.dumps(node_dynamic_map);
		with open('states.json', 'w') as outfile: outfile.write(json_str);

	'''
	SIV Model
	for each time step:
		for each node:
			if susceptible, look at neighbors
				for each neighbor
					if neighbor is infected, flipCoin on beta with potentialState='INFECTED'
					else do nothing
					break when the current node we're looking at gets infected
			if still susceptible
				flipCoin on theta with potentialState'VIGILANT'
			if infected 
				flipCoin on delta with potentialState='VIGILANT'
			if vigilant
				flipCoin on gamma with potentialState='SUSCEPTIBLE'
	'''

	def SIVmodel(self):
		for i in xrange(self.time):
			for node in self.nodes:
				if node.getState() == 'SUSCEPTIBLE':
					for neighbor in node.getNeighbors():
						if neighbor.getState() == 'INFECTED':
							success = node.flipCoin(self.beta, 'INFECTED')
							#stop looping through the neighbors if the node we're looking at is infected
							if success:
								break
				if node.getState() == 'SUSCEPTIBLE':
					node.flipCoin(self.theta, 'VIGILANT')
				elif node.getState() == 'INFECTED':
					node.flipCoin(self.delta, 'VIGILANT')
				elif node.getState() == 'VIGILANT':
					node.flipCoin(self.gamma, 'SUSCEPTIBLE')

	'''
	SEIR Model
	for each time step:
		for each node:
			if susceptible, look at neighbors
				for each neighbor
					if neighbor is infected, flipCoin on beta with potentialState='EXPOSED'
					else do nothing
					break when the current node we're looking at gets infected
			if exposed:
				flipCoin on epsilon with potentialState='INFECTED'
			if infected:
				flipCoin on delta with potentialState='RECOVERED'
			if recovered:
				flipCoin on gamma with potentialState='SUSCEPTIBLE'
	'''

	def SEIRmodel(self):
		for i in xrange(self.time):
			for node in self.nodes:
				if node.getState() == 'SUSCEPTIBLE':
					for neighbor in node.getNeighbors():
						if neighbor.getState() == 'INFECTED':
							success = node.flipCoin(self.beta, 'EXPOSED')
							#stop looping through the neighbors if the node we're looking at is exposed
							if success:
								break
				elif node.getState() == 'EXPOSED':
					node.flipCoin(self.epsilon, 'INFECTED')
				elif node.getState() == 'INFECTED':
					node.flipCoin(self.delta, 'RECOVERED')
				elif node.getState() == 'RECOVERED':
					node.flipCoin(self.gamma, 'SUSCEPTIBLE')

	'''
	SEIV Model
	for each time step:
		for each node:
			if susceptible, look at neighbors
				for each neighbor
					if neighbor is infected, flipCoin on beta with potentialState='EXPOSED'
					else do nothing
					break when the current node we're looking at gets infected
			if still susceptible:
				flipCoin on theta with potentialState='VIGILANT'
			if exposed:
				flipCoin on epsilon with potentialState='INFECTED'
			if infected:
				flipCoin on delta with potentialState='RECOVERED'
			if recovered:
				flipCoin on gamma with potentialState='SUSCEPTIBLE'

	'''

	def SEIVmodel(self):
		for i in xrange(self.time):
			for node in self.nodes:
				if node.getState() == 'SUSCEPTIBLE':
					for neighbor in node.getNeighbors():
						if neighbor.getState() == 'INFECTED':
							success = node.flipCoin(self.beta, 'EXPOSED')
							#stop looping through the neighbors if the node we're looking at is exposed
							if success:
								break
				if node.getState() == 'SUSCEPTIBLE':
					node.flipCoin(self.theta, 'VIGILANT')
				elif node.getState() == 'EXPOSED':
					node.flipCoin(self.epsilon, 'INFECTED')
				elif node.getState() == 'INFECTED':
					node.flipCoin(self.delta, 'VIGILANT')
				elif node.getState() == 'VIGILANT':
					node.flipCoin(self.gamma, 'SUSCEPTIBLE')
