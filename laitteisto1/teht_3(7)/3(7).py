import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt

# 1.

A = np.array([[-1, 2], [3, -5]])
B = np.array([[2, 0], [-1, 4]])

result_2A3B = 2*A + 3*B
result_AB = A - B

print("2A + 3B: \n", result_2A3B)
print("\nA - B: \n", result_AB)

# 2.
# a)

left_a = np.array([[5, 3], [2, 1]])
right_a = np.array([[9], [4]])

result_a = la.inv(left_a).dot(right_a)
print("\n2a)\n", result_a)

# b)

left_b = np.array([[2, 1, 1], [1, 3, 1], [2, 1, 2]])
right_b = np.array([[6], [2], [9]])

result_b = la.inv(left_b).dot(right_b)
print("\n2b)\n", result_b)

# c)

left_c = np.array([[1, 1, 3], [3, 1, 1], [2, 1, 2]])
right_c = np.array([[-1], [5], [2]])

try:
    result_c = la.inv(left_c).dot(right_c)
    print("\n2c)\n", result_c)
except la.LinAlgError:
    print("\n2c)\nSingular matrix")