import networkx as nx
import os
class computerplot(object):
	def __init__(self):
		self.graph = nx.Graph()
		self.current = "/" # current path
		
	def main(self):
		going = True
		self.folderScan = {}
		
		while going=True:
	
	def graph(x,y): # x is from (fullpath), y is to (filename)
		folders = x.split()
		self.graph.add_edge( folders[ len(folders)], y) # last element in folders is the upper foldername
		
	def populate(self, fullpath):
		files = os.listdir()
		for file in files:
			
			filePath = fullpath+"/"+file
			if not os.path.isdir(filePath): #is file
			
				graph(fullPath, file) # graph them
				del files
		
		