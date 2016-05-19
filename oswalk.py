from __future__ import division
import os
import networkx as nx
import matplotlib.pyplot as plt

def getFolderName(fullpath, backnum): # backnum 1 = folder currently in. 2= the folder where the folder we are currently are in is.
	x = open("ssh.txt")
	folders = fullpath.split(x.readline())
	x.close()
	
	toret = folders[ len(folders)-backnum ]
	
	if backnum > len(folders): # /selbulantimelapsv2 (backnum 2 = "/")
		toret = "/"
	return toret
	
graph = nx.MultiGraph()
graph.add_node("/")
loopcount = 0
for root, dirs, files in os.walk("/", topdown=False):
	for name in files and dirs:
		loopcount += 1
		print loopcount/(len(files)+len(dirs))
		
		path = os.path.join(root, name)
		base = os.path.basename(path)
		dirname = getFolderName(path, 2)
		
		#print dirname + "==>" + base
		
		graph.add_edge(dirname,base, color='blue')

		
print "drawing"
nx.draw(graph)
plt.show()
