import networkx as nx
import os
import random

class computerplot(object):
	def __init__(self):
		self.graph = nx.Graph()
		self.current = "/" # current path
		
	def main(self):
		going = True
		self.folderScan = {} # where os.listdir() content goes
		fullpath = "/"
		
		while going = True:
			currentFolders = self.populate(fullpath)
			fullpath += "/" + random.choise( currentFolders ) # random next folder
 	
	def graph(x,y): # x is from (fullpath), y is to (filename)
		folders = x.split()
		self.graph.add_edge( folders[ len(folders)-1], y) # last element in folders is the upper foldername
		
	def populate(self, fullpath):
		files = os.listdir()
		for file in files:
			
			filePath = fullpath+"/"+file
			
			self.graph(fullPath, file) # network graph them
			
			if not os.path.isdir(filePath): 
				del file
		
		self.folderScan[fullpath] = files
		return files
		