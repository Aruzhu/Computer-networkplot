import networkx as nx
import os

graph = nx.Graph()

current = "/" # current path

going = True
while going=True:

	for file in os.listdir(current): # disk folder loop
		fullpath = current+"/"+file
		if os.path.isdir(fullpath):
			currentfolders.append(file)
		
		graph.add_edge(current, file)

	