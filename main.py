import networkx as nx
import os

graph = nx.Graph()

current = "/" # current path
currentfolders = [] #all folders in the current folder
going = True
while going=True:

	for file in os.listdir(current):
		fullpath = current+"/"+file
		if os.path.isdir(fullpath):
			currentfolders.append(file)
		
		graph.add_edge(current, file)
	
	