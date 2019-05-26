#################################### MathLib #####################################

'''
Linear Algebra Lib - Gauss-Jordan
This code implements a simple Gauss-Jordan algorithm to solve linear systems. This
code is not optimize in any way therefor should never been used in any application

Algorithm complexity = O(n^3) + O(n^2) = O(n^3) 
'''

def pivotMatrix(A):
	## Evaluating each element of the matrix
	for i in xrange(len(A)-1):
		for j in xrange(i+1, len(A)):
			n1 = A[j][i]
			if n1 == 0:
				for k in xrange(i, len(A)):
					if A[k][i] != 0:
						swapLine(A, i, k)
						n1 = A[j][i]
			n2 = A[i][i]

			if n2 == 0:
				continue

			div = n1/n2
			A[j] = sumLines(multipliLines(A[i], -div), A[j])
	return A


def multipliLines(L, x):
	newLine = []
	for i in xrange(len(L)):
		newLine += [L[i]*x]
	return newLine

def sumLines(L1,L2):
	newLine = []
	for i in xrange(len(L1)):
		newLine += [L1[i]+L2[i]]
	return newLine

def swapLine(A, i, j):
	newI = []
	newJ = []
	for index in xrange(len(A)+1):
		newI += [A[j][index]]
		newJ += [A[i][index]]
	A[i] = newI
	A[j] = newJ

def printMatrix(A):
	for i in A:
		print '|\t'
		for j in i:
			print'%.1f' %(j), '\t'
		print "\t|"

A = [[1.0, -1.0, 2.0, -1.0, -8.0], [2.0, -2.0, 3.0, -3.0, -20], [1.0, 1.0, 1.0, 0.0, -2.0], [1.0, -1.0, 4.0, -3.0, 4.0]]
printMatrix(A)
print '\n\n'
printMatrix(pivotMatrix(A))
