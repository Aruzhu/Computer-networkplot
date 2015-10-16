import networkx as nx
import os
import random

class computerplot(object):
	def __init__(self):
		self.graph = nx.Graph() # ze ram eater
		self.current = "/" # current path
		self.fucked = False
	
	def main(self):
		going = True
		self.folderScan = {1:2} # where os.listdir() content goes
		fullpath = "/"
		
		while going == True:
			currentFolders, fucked = self.populate(fullpath)
			#print currentFolders
			
			if fucked == True:
				fullpath = fullpath[ 0: len( getUpperFolder(fullpath) )+1 ] # remove the upperfolder, +1 because of the backslash
			else:
				if currentFolders: # if not empty
				
					if fullpath != "/": #see issue #1
						fullpath += "/" + random.choice( currentFolders ) # random next folder
					else:
						fullpath += random.choice( currentFolders )
				
				else: # if empty
				
					self.deleteOccurance(fullpath)
				
	def getUpperFolder(self, fullpath):
		folders = fullpath.split("/")
		return folders[ len(folders)-1 ]
		
	def graphFunc(self, x, y): # x is from (fullpath), y is to (filename)
		self.graph.add_edge( self.getUpperFolder(x), y) # last element in folders is the upper foldername
		
	def deleteOccurance(self, fullpath):
	
		upperfolder = self.getUpperFolder(fullpath)
		print "upperfolder: " + upperfolder
		self.folderScan[ fullpath ].remove( upperfolder )
		# deleting the occurance of done folder in the folderscan entry of the Upperfolder. So that it wont be plotted twice
	
	def populate(self, fullpath):
		fucked = False
		files = []
		# try:
		
		files = os.listdir(fullpath) # list all files and folders
		
		# except WindowsError: # no premmision, se issue 2
			# if os.path.isdir(fullpath):
				# fucked = True
				# self.deleteOccurance(fullpath)
				# files = []

			 
		for file in files:
		
			filePath = fullpath+"/"+file # path to the current file
			self.graphFunc(fullpath, file) # network graph them
			
			if os.path.isfile(filePath): # if not directory
				print "not folder"
				files.remove(file)
		
		if bool(files): # if not empty
			print files
			self.folderScan[fullpath] = files
		print self.folderScan.keys() == files
		return files, fucked
computerplot = computerplot()
computerplot.__init__()
computerplot.main()