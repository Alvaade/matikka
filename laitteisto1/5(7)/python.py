import numpy as np
import numpy.linalg as la
import sympy as sp

x = sp.symbols('x')

# 1a)

A = np.array([[-1, 2], [3, 1]])
B = np.array([[0, 1, 3], [2, -3, 5]])
print(f"1a) \n{np.dot(A,B)}")

# 1b)

A = np.array([[1, 3, 5], [0, -2, 1], [2, -1, 4]])
B = np.array([[1], [-3], [-1]])
print(f"1b) \n{np.dot(A,B)}")

# 1c)

A = np.array([[2, 0, 1], [1, -3, 4], [0, 1, 5]])
B = np.array([[3], [-5], [7]])
print(f"1c) \n{np.dot(A,B)}")

# 1d)

A = np.array([[1, -4, 2], [3, 0, -2], [2, 1, 0]])
B = np.array([[5, 1, -1], [-2, 1, 3], [0, 3, 4]])
print(f"1d) \n{np.dot(A,B)}")

print()

# A

A = np.array([[4, 9, 0], [-3, 7, -11]])
print(f"1. AT \n {np.transpose(A)}")

# B

B = np.array([[8, 9], [-3, 12], [0, -1], [7, 1]])
print(f"1. BT \n {np.transpose(B)}")

# 1a)

A = np.array([[5, -6], [8, 10]])
print(f"1a) \n {round(la.det(A))}")

# 1b)

A = sp.Matrix([[1-x, -x], [x, 1-x]])
print(f"1b) \n {(sp.det(A))}")

# 2a)

A = np.array([[2, 3, 4], [-2, -1, 1], [5, 3, 2]])
print(f"2a) \n {round(la.det(A))}")

# 2b)

A = np.array([[3, 15, 7], [0, -4, 0], [3, 2, 3]])
print(f"2b) \n {round(la.det(A))}")

# 3

A = np.array([[-2, 0, 8, 5], [3, -1, 2, 1], [4, 7, 6, 2], [1, 0, 2, 3]])
print(f"3) \n {round(la.det(A))}")