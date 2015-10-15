import networkx as nx
import os
import random

class computerplot(object):
	def __init__(self):
		self.graph = nx.Graph() # ze ram eater
		self.current = "/" # current path
	
	def main(self):
		going = True
		self.folderScan = {} # where os.listdir() content goes
		fullpath = "/"
		
		while going == True:
			currentFolders = self.populate(fullpath)
			print currentFolders
			if currentFolders: 
				fullpath += "/" + random.choice( currentFolders ) # random next folder
			else: # if empty
				del self.folderscan[fullpath][ self.folderscan[fullpath].index(fullpath) ]
				# deleting the occurance of done folder in the folderscan entry of the Upperfolder. So that it wont be plotted twice
			
	def getUpperFolder(self, fullpath):
		folders = fullpath.split("/")
		return folders[ len(folders)-1 ]
		
	def graphFunc(self, x, y): # x is from (fullpath), y is to (filename)
		self.graph.add_edge( self.getUpperFolder(x), y) # last element in folders is the upper foldername
		
	def populate(self, fullpath):
		files = os.listdir(fullpath) # list all files and folders
		
		for file in files:
			filePath = fullpath+"/"+file # path to the current file
			
			self.graphFunc(fullpath, file) # network graph them
			
			if not os.path.isdir(filePath): # if not directory
				del file
		
		if files: # if not empty
			self.folderScan[fullpath] = files
		return files
computerplot = computerplot()
computerplot.__init__()
computerplot.main()