import random

class Node:

	def __init__(self, id):
		self.id = id #node id, should be an int
		#Options include: 'SUSCEPTIBLE', 'INFECTED', 'VIGILANT', 'RECOVERED', 'EXPOSED'
		self.possible_states = ['SUSCEPTIBLE', 'INFECTED', 'VIGILANT', 'RECOVERED', 'EXPOSED']
		self.state = 'SUSCEPTIBLE'
		self.neighbors = []

	def flipCoin(self, prob, potentialState):
		#takes in a probability and a potential state that it could change to
		#returns true if the state was changed and false otherwise
		if not potentialState in self.possible_states:
			return False 
		if random.random() < prob:
			self.state = potentialState
			return True 
		return False


	def getState(self):
		return self.state

	def setState(self, newState):
		if newState in self.possible_states:
			self.state = newState
			return True 
		return False

	def addNeighbor(self, n):
		self.neighbors.append(n)

	def getDegree(self):
		return len(self.neighbors)

	def getNeighbors(self):
		return self.neighbors

	def getThis(self):
		return self
