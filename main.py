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
		self.folderScan = {} # where os.listdir() content goes
		fullpath = "/"
		
		while going == True:
			currentFolders, fucked = self.populate(fullpath)
			#print currentFolders
			
			if fucked == True:
				fullpath = fullpath[ 0: len( self.getFolderName(fullpath,1) )+1 ] # remove the upperfolder, +1 because of the backslash
			else:
				if currentFolders: # if not empty
				
					if fullpath != "/": #see issue #1
						fullpath += "/" + random.choice( currentFolders ) # random next folder, continue going deeper
					else:
						fullpath += random.choice( currentFolders )
				
				else: # if empty
				
					self.deleteOccurance(fullpath)
				

	def getFolderName(self, fullpath, backnum):
		folders = fullpath.split("/")
		toret = folders[ len(folders)-backnum ]
		
		if backnum > len(folders): # /selbulantimelapsv2 (backnum 2 = "/")
			toret = "/"
		return toret
	
	def graphFunc(self, x, y): # x is from (fullpath), y is to (filename)
		self.graph.add_edge( self.getFolderName(x,1), y) # last element in folders is the upper foldername
		
	def deleteOccurance(self, fullpath):
	
		upperfolder = self.getFolderName(fullpath,1)
		print "upperfolder: " + upperfolder + "	at " + fullpath
		
		
		
		key = fullpath[0: fullpath.find( self.getFolderName(fullpath, 2) )] + self.getFolderName(fullpath, 2) # need fullpath without the first folder and "/"
		#fullpath[ 0: self.getFolderName(fullpath, 2) ]
		print "key used = " + str(key)
		
		if key not in self.folderScan.keys():
			fullpath = "/"
			
		self.folderScan[ key ].remove( upperfolder )
		# deleting the occurance of done folder in the folderscan entry of the Upperfolder. So that it wont be plotted twice
	
	def populate(self, fullpath):
		fucked = False
		files = []

		
		files = os.listdir(fullpath) # list all files and folders
		folders = []
		
		for file in files:
			if fullpath != "/": 
				filepath = fullpath+"/"+file # path to the current file
			else: # if first scan
				filepath = fullpath+file
				
			self.graphFunc(fullpath, file) # network graph them
			
			if os.path.isfile(filepath): # if not directory
				files.remove(file)
			elif os.path.isdir(filepath):
				folders.append(file)
		
		if bool(folders): # if not empty
			print folders
			self.folderScan[fullpath] = files
		
		if "System Volume Information" in folders: #acts like folder but is a file
			folders.remove("System Volume Information")
		return folders, fucked
		
computerplot = computerplot()
computerplot.__init__()
computerplot.main()