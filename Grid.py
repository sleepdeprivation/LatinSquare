import copy

class Square:

	G = []
	n = 0
	
	def __init__(self, n):
		for i in range(n):
			temp = []
			for k in range(n):
				temp.append(-1)
			self.G.append(temp)
		self.n = n
		self.standardTemplate()

	#make a deep copy of yourself and return it
	def deepCopy(self):
		S = Square(self.n)
		S.G = copy.deepcopy(self.G)
		return S

	#make a square that looks like this:
	'''
		0 1 2 3 4 
		1 X X X X 
		2 X X X X 
		3 X X X X
		4 X X X X
	'''
	def standardTemplate(self):
		for i in range(self.n):
			self.G[i][0] = i
			self.G[0][i] = i

	'''
		print positive integers (and zero) as themselves,
		and negative integers as 'X'
	'''
	def printOut(self):
		for i in range(self.n):
			s = ""
			for k in range(self.n):
				if(self.G[i][k] >= 0):
					s += str( self.G[i][k] )
				else:
					s += "X"
				s += " "
			print s

	#The whole matrix is filled (there are no -1 entries)
	def filled(self):
		for i in range(self.n):
			for k in range(self.n):
				if(self.G[i][k] == -1):
					return False
		return True

	#check if you can place s in row r column c
	def canPlace(self, r, c, s):
		if( not (self.rowContains(r, s) or self.colContains(c, s)) ):
			return True
		return False

	#check if row r contains s
	def rowContains(self, r, s):
		for i in range(self.n):
			if(self.G[r][i] == s):
				return True
		return False

	#check if coumn c contains s
	def colContains(self, c, s):
		for i in range(self.n):
			if(self.G[i][c] == s):
				return True
		return False


def main():
	s = Square(5)
	s.printOut()

if __name__ == "__main__":
	main()
