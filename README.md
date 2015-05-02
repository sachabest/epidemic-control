# nets312
## NES 312 Project - Epidemic Control
### Spring 2015

Sacha Best, Corey Loman, Vincent Gubitosi

This project is divided into two sections: datavis and analysis. 

The analysis section is used to extract relevant information from the original 9.4 million node contact graph in Sierra Leona, process that information, and run viral spreading models on it. The files included in that folder are as follow:

* aggregator.py: contains the logic required to run the simulation
* network.py: contains initialization of reading in subgraph
* node.py: node class for a node in our graph
* project1.py: one implementation of how to load the data and extract a subgraph
* parser.py: another implementation of how to load the data and extract a subgraph
* spreadingModel.py: implementation of the six different spreading models discussed in Prakash's paper
* seedingStrategies.py: implementation of seeding strategies to spread information based on largest degrees, eigenvector centrality, k-core decomposition (explained in Kitsak's paper), and cascading size (which utilizes the Hill Climbing Algorithm)
* geolocator.py - creates a map of nodes to their latitude, longitude, population size, and capacity from SLE_locations.txt in output

The datavis section is a NodeJS web application that uses sigma.js to visualize a small subset of the graph created by the analysis section. This graph is animated over time to show how Ebola spread through Sierra Leone in 2014. Relevant files include:

* app.js: the main NodeJS routing file
* main.js: the javascript file loaded clientside to control the graph
* main.css: the main css file
* views/: jade template files for the main view page    
* *.gephi: Gephi graph engine files used to run ForceAtlas2 and other visualization tools before sending to sigma.js. This was done in order to prvent clientside machines from doing intensive graph algorithms.
* sample.gexf: the Gephi output used by sigma.js
* states.json: the infected/recovered/susceptible data for each node at each timestep

Helpful Resources:
* http://nets312.sachabest.com - Data Visualization of Subgraph
* http://networks.asc.upenn.edu/?page_id=325 - Project Blog
* http://www.vbi.vt.edu/ndssl/ebola/ebola-data - Dataset Source Page
* https://docs.google.com/document/d/1NI73mFVAOFmrqfsX0XGiJL5o2gze5K-YjJbx6plw38k/edit?usp=sharing - Final Report
* https://drive.google.com/file/d/0B4O42U-pfdyhcmNTbGhKU0tLcEE/view?usp=sharing - Final Presentation PowerPoint
* http://people.cs.vt.edu/~badityap/papers/gen-threshold-kais12.pdf - Prakash's Research Paper
* http://www.nature.com/nphys/journal/v6/n11/fig_tab/nphys1746_ft.html - Kitsak's Research Paper
