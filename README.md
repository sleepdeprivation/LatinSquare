
## The Grid.Square class


### make a deep copy of yourself and return it
	def deepCopy(self):
	
	
### make a square that looks like this:
	'''
		0 1 2 3 4 
		1 X X X X 
		2 X X X X 
		3 X X X X
		4 X X X X
	'''
	def standardTemplate(self):
	
	
### The whole matrix is filled (there are no -1 entries)
	def filled(self):


### check if you can place s in row r column c
	def canPlace(self, r, c, s):


### check if row r contains s
	def rowContains(self, r, s):


### check if coumn c contains s
	def colContains(self, c, s):
	
	
## LatinSquare.LatinSquareSolver class

   	solved = []	holds all the solutions generated by the below functions

    ###find all possible solutions
    def solve(self, LS):

    ###stop as soon as you find 1 solution
    def solveOne(self, LS):
    
If this class is called as main(), it will brute force search for all 5x5 latin squares



