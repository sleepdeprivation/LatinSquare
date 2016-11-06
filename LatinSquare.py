import copy
import Grid

'''Brute force searches for all latin squares of a given size'''
class LatinSquareSolver:
    solved = []	#holds all the solutions generated by the below functions

    #find all possible solutions
    def solve(self, LS):
	    if(LS.filled()):
		    self.solved.append(LS)
	    else:
		    for i in range(LS.n):		#rows
			    for k in range(LS.n):		#columns
				    if(LS.G[i][k] == -1):		#it hasn't been filled			
					    for s in range(LS.n):
						    if(LS.canPlace(i, k, s)):	#latin square property
							    R = LS.deepCopy()
							    R.G[i][k] = s		#let's try it then
							    self.solve(R)		#recurse
					    return

    #stop as soon as you find 1 solution
    def solveOne(self, LS):
	    if(LS.filled()):
		    self.solved.append(LS)
		    return True
	    else:
		    for i in range(LS.n):
			    for k in range(LS.n):
				    if(LS.G[i][k] == -1):
					    for s in range(LS.n):
						    if(LS.canPlace(i, k, s)):
							    R = LS.deepCopy()
							    R.G[i][k] = s
							    if(self.solveOne(R)):
								    return True
					    return False

def main():
	s = Grid.Square(5)
	solver = LatinSquareSolver()
	solver.solve(s)
	for i in solver.solved:
		i.printOut()
		print '\n',

	print "the number of squares: " + str(len(solver.solved))

if __name__ == "__main__":
	main()