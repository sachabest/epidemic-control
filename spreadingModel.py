'''assume I have a list of Nodes
GENERAL MODEL

variables include: 
-beta (trasmission probability over an edge if susceptible)
-delta (healing probability once infected)
-gamma (immunization-loss probability once recovered or vigilant)
-epsilon (virus-maturation probability once exposed)
-theta (direct-immunization probability when susceptible)

for each time step:
	for each node:
		if susceptible, look at neighbors
			if neighbor is infected, flipCoin on beta with potentialState='INFECTED'
			else do nothing
		if susceptible
			flipCoin on theta with potentialState='VIGILANT'
		if INFECTED


'''