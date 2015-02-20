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