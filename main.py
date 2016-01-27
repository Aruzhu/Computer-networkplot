import networkx as nx
import os
import random

plotprint = True
functionstartprint = False
filePrison = ["Documents and Settings", "System Volume Information"] #bad bad files
class computerplot(object):
	def __init__(self):
		self.graph = nx.Graph() # ze ram eater
		self.current = "/" # current path
		self.fucked = False
	def functionstart(self, name):
		if functionstartprint == True:
			print("entering " + name + " function")
	def main(self):
		self.functionstart("main")
		
		going = True
		self.folderScan = {} # where os.listdir() content goes
		fullpath = "/"
		
		while going == True:
			fullpath = self.CheckPopulate(fullpath) # check the fullpath, before populating to withstand errors.
		
			currentFolders, fucked = self.populate(fullpath)
			#print currentFolders
			
			if fucked == True: # did not have premission to scan the folder
				fullpath = fullpath[ 0: len( self.getFolderName(fullpath,1) )+1 ] # remove the upperfolder, +1 because of the backslash
			else: # if everything works
			
				if currentFolders: # if not empty
					if fullpath != "/": #see issue #1
						fullpath += "/" + random.choice( currentFolders ) # random next folder, continue going deeper
					else:
						fullpath += random.choice( currentFolders )
				
				else: # if empty
				
					self.deleteOccurance(fullpath) # delete it form folderscan
					
					files = self.folderScan[ self.GetKeyFolderScan(fullpath)]
					
					if files != []: # still not empty, go deeper 
						fullpath = self.RemoveCurrentFolder(fullpath) # removing first folder and "/"
						fullpath += "/" + random.choice( self.folderScan[ self.GetKeyFolderScan(fullpath)] ) 
					else: # a1
						# need to loop upwards until it finds a folder with unplotted folders
						print("finding closest undone folder, plotted all of them.  calling emptyloop, see a1")
						fullpath = self.EmptyLoop(fullpath)
						
	def EmptyLoop(self, fullpath): # loop until folderscan list is not empty
		self.functionstart("Emptyloop")
		files = self.folderScan[ self.GetKeyFolderScan(fullpath)]
		
		if "*.*" in files: # is this really necessary?
			del files[ files.index("*.*")]
			print("indexed")
		
		while files == []:
			del self.folderScan[ self.GetKeyFolderScan(fullpath)]
			
			fullpath = self.RemoveCurrentFolder(fullpath)
			files = self.folderScan[ self.GetKeyFolderScan(fullpath) ]
			
		return fullpath
		
	def RemoveCurrentFolder(self, fullpath): # remove the current folder from fullpath
		self.functionstart("RemoveCurrentFolder")
		fullpath = fullpath[0: fullpath.find( self.getFolderName(fullpath, 2) )] + self.getFolderName(fullpath, 2)
		#notice that we remove up to the secound folder and then adds it back again.
		return fullpath
	
	def getFolderName(self, fullpath, backnum): # backnum 1 = folder currently in. 2= the folder where the folder we are currently are in is.
		self.functionstart("getFolderName")
		folders = fullpath.split("/")
		toret = folders[ len(folders)-backnum ]
		
		if backnum > len(folders): # /selbulantimelapsv2 (backnum 2 = "/")
			toret = "/"
		return toret
		
		
	def graphFunc(self, x, y): # x is from (fullpath), y is to (filename)
		self.functionstart("graphFunc")
		if plotprint == True:
			print(self.getFolderName(x,1) + " ==> " + y)
		self.graph.add_edge( self.getFolderName(x,1), y) # last element in folders is the upper foldername
	
	def findOccurance(self, string, tofind): # does not work with letter of tofind more than 1. we dont need that either
		self.functionstart("findOccurance")
		occs = 0
		for i in string:
			if i == tofind:
				occs += 1
		return occs
	
	def GetKeyFolderScan(self,fullpath): # get key for the FolderScan dictionary
		self.functionstart("GetKeyFolderScan")
		
		self.upperfolder = self.getFolderName(fullpath,1)
		
		if self.findOccurance("/", fullpath) != 1: # if more than one "/" in fullpath
			key = self.RemoveCurrentFolder(fullpath) # remove current folder from fullpath, i.e we get the folder name where the folder we are in is, i.e the key.
		elif self.findOccurance("/", fullpath) == 1: # /selbulantimelapsv2, /xfoldername
			key = "/"
		
		if key == "":
			if "/" in self.folderScan.keys():
				key = "/"
			else:
				plt.savefig(platform.system()+".jpg")
				exit()
		if key not in self.folderScan.keys(): # if not valid key
			print("key not found in fullpath")
			print("key used: " + key)
		
		return key
	def deleteOccurance(self, fullpath):# deleting the occurance of done folder in the folderscan entry of the Upperfolder. So that it wont be plotted twice
		self.functionstart("deleteOccurance")
		
		key = self.GetKeyFolderScan(fullpath)
		
		if self.upperfolder in self.folderScan[ key]:
			self.folderScan[ key ].remove( self.upperfolder )
		
	
	def CheckPopulate(self, fullpath): # check if fullpath can be scanned and works.
		self.functionstart("CheckPopulate")
		
		if fullpath != "/":
			print(fullpath)
			
			try : # if it fails to scan i.e premission error, 
				files = os.listdir(fullpath)
			except: #a4
				print("calling emptyloop from a4")
				print(fullpath.find("*.*"))
				fullpath = self.EmptyLoop(fullpath) # this returns fullpath with *.*
				#self.CheckPopulate(fullpath)
		return fullpath
		
	def populate(self, fullpath): # scan the fullpath directory
		
		fucked = False
		files = []
		
		files = os.listdir(fullpath) # list all files and folders, is getting files for some reason
		folders = []
		
		for file in files:
			if fullpath != "/": # if not first scan
				filepath = fullpath+"/"+file # path to the current file
			else: # if first scan, / + file
				filepath = fullpath+file
				
			self.graphFunc(fullpath, file) # network graph them
			
			if os.path.isfile(filepath): # if not directory
				files.remove(file)
			elif os.path.isdir(filepath):
				folders.append(file)
		
		if bool(folders): # if not empty
			self.folderScan[fullpath] = files
		
		for file in filePrison: # delete the buggy ones.
			if file in folders:
				folders.remove(file)
		return folders, fucked

#run it!
computerplot = computerplot()
computerplot.__init__()
computerplot.main()