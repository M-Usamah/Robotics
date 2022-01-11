""" 
(C) Write a program in Python that determines whether a matrix is orthogonal.
(D) Use this program to investigate whether (D) metrix is orthogonal.
"""


import numpy as np

def check_orthogonal(M):

    if len(np.shape(M)) != 2:
        print("error: input is not a matrix")
        return

    dim = np.shape(M)[0]

    if dim != np.shape(M)[1]:
        print("error: input is not a square matrix")
        
    A = np.dot(M, M.T)
    if np.array_equal(A, np.identity(dim)):
        print("The matrix is orthogonal")
    else:
        print("matrix is not orthogonal")

print()
print()
print(" D= 1  | 2      2     -1|")
print("    /  | 2     -1      2|")
print("    3  |-1      2      2| ")
D = 1./3. * np.array(
[[2, 2, -1],
[2, -1, 2],
[-1, 2, 2]])
check_orthogonal(D)
print("----------------------------------")

print()
print()