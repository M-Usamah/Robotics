'''
 Exercise 1: Linear Algebra

a) Consider the matrices

("symmetric positive definite")
'''

def transpose(mat, tr, N):
	for i in range(N):
		for j in range(N):
			tr[i][j] = mat[j][i]


def isSymmetric(mat, N):
	
	tr = [ [0 for j in range(len(mat[0])) ] for i in range(len(mat)) ]
	transpose(mat, tr, N)
	for i in range(N):
		for j in range(N):
			if (mat[i][j] != tr[i][j]):
				return False
	return True


def check_symmetric_func(mat):
    if (isSymmetric(mat, 2)):
	    print ("Yes")
    else:
	    print ("Not")

print("---------------------------------------------")

print("   ")
print(" A=   | 0.25     0.1 |")
print("      | 0.2      0.5 |")
print("(A) matrices is ")
check_symmetric_func([ [ 0.25,0.1 ], [ 0.2,0.5 ] ])
print("symmetric positive definite")
print("---------------------------------------------")


print("   ")
print(" b=   | 0.25    -0.3 |")
print("      |-0.3      0.5 |")
print("(B) matrices is ")
check_symmetric_func([ [ 0.25,-0.3 ], [ -0.3,0.5 ] ])
print("symmetric positive definite")
print("---------------------------------------------")



print("   ")
print(" c=   | -3      0 |")
print("      |  0      1 |")
print("(c) matrices is ")
check_symmetric_func([ [ -3,0 ], [ 0,1 ] ])
print("symmetric positive definite")
print("---------------------------------------------")


