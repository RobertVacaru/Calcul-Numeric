import numpy as np

# functions that need to be implemented
from tema2 import substitution_method, get_inv, gauss_algorithm, get_diff

# dummy functions that mirror standard methods from libraries (but you'll have to discover them)
from tema2 import get_norm, lib_solve, lib_inv

from tema2 import plot_matrix_evolution

np.random.seed(10)
np.set_printoptions(suppress=True)

n = 10
A = np.random.randint(low=1, high=100, size=n * n).reshape(n, n)
A = np.triu(A)
b = np.random.randint(low=1, high=100, size=n)
print("A:" + f'{A}')
print("b:" + f'{b}')
# A = [[10, 16, 65, 29, 90, 94, 30, 9, 74, 1],
#      [0, 37, 17, 12, 55, 89, 63, 34, 73, 79],
#      [0, 0, 55, 78, 70, 14, 26, 14, 93, 87],
#      [0, 0, 0, 13, 66, 32, 58, 37, 28, 19],
#      [0, 0, 0, 0, 95, 12, 29, 75, 89, 10],
#      [0, 0, 0, 0, 0, 12, 18, 47, 8, 76],
#      [0, 0, 0, 0, 0, 0, 6, 5, 72, 89],
#      [0, 0, 0, 0, 0, 0, 0, 16, 7, 86],
#      [0, 0, 0, 0, 0, 0, 0, 0, 43, 58],
#      [0, 0, 0, 0, 0, 0, 0, 0, 0, 24]]
# b = [4, 30, 17, 85, 83, 15, 52, 80, 18, 51]
x = substitution_method(A, b, n)
print("Resulted x:" + f'{x}')
# diff = get_diff(A, b, x, n)
diff = A @ x - b
print("Diff:"+f'{diff}')
# A = [[54, 26, 49, 18, 33],
#      [82, 81, 42, 91, 13],
#      [31, 82, 18, 17, 1],
#      [32, 74, 65, 39, 23],
#      [97, 67, 68, 63, 96]]
# b = [28, 83, 63, 78, 49]
n = 5
A = np.random.randint(low=1, high=100, size=n * n).reshape(n, n)
b = np.random.randint(low=1, high=100, size=n)
A = [[54, 26, 49, 18, 33],
      [82, 81, 42, 91, 13],
      [82, 81, 42, 91, 13],
      [32, 74, 65, 39, 23],
      [97, 67, 68, 63, 96]]
b = [28, 83, 63, 78, 49]
print("\nA:" + f'{A}')
print("b:" + f'{b}')
A_gauss, b_gauss, evo = gauss_algorithm(A, b, n=n)
print("\nA gauss and b gauss")
print(A_gauss)
print(b_gauss)
x_gauss = substitution_method(A_gauss, b_gauss, n=n)
print("\nResults after substitution method")
print(x_gauss)

print("\nGet the norm of the output results")
print(get_norm(A @ x_gauss - b))
print("\nUsing a library to compute everything")
x_lib = lib_solve(A, b)
print(x_lib)
print("Norm:" + f'{get_norm(x_gauss - lib_inv(A) @ b)}')
print("\nDifferences between norms:" + f'{get_norm(x_gauss - lib_inv(A) @ b)}')
print("A:" + f'{A}')

print("\nInverse of matrix X matrix:\n"+f'{get_inv(A)@A}')

print("\nDifference between library inverse of matrix and our inverse:\n"+f'{lib_inv(A)-get_inv(A)}')
