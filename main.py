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
	
	def findOccurance(self, string, tofind):
		occs = 0
		for i in string:
			if i == tofind:
				occs += 1
		return 
	
	def deleteOccurance(self, fullpath):
	
		upperfolder = self.getFolderName(fullpath,1)
		print "upperfolder: " + upperfolder + "	at " + fullpath
		
		
		if len(fullpath.split("/")) != 1:
			key = fullpath[0: fullpath.find( self.getFolderName(fullpath, 2) )] + self.getFolderName(fullpath, 2) # need fullpath without the first folder and "/"
			# in other words the fullpath of the upperupperfolder (i.e where the folder we are in is) /upperupperfolder/upperfolder/where we are
		else: # /selbulantimelapsv2, /xfoldername
			key = "/"

		print "key used = " + str(key)
		
		for i in self.folderScan[key]:
			print i
		self.folderScan[ key ].remove( upperfolder )
		# deleting the occurance of done folder in the folderscan entry of the Upperfolder. So that it wont be plotted twice
	
	def populate(self, fullpath):
		fucked = False
		files = []

		try:
			files = os.listdir(fullpath) # list all files and folders
		except:
			fucked = True
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
			self.folderScan[fullpath] = files
		
		if "System Volume Information" in folders: #acts like folder but is a file
			folders.remove("System Volume Information")
		return folders, fucked
		
computerplot = computerplot()
computerplot.__init__()
computerplot.main()