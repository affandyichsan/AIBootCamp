import numpy as np

matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("original Matrix : \n", matrix)

transpose = matrix.T
print("transpose:\n", transpose)

another_matrix = np.array([[9,8,7], [6,5,4],[3,2,1]])
print("addition : \n", matrix + another_matrix)
print("multiplication : \n", matrix * another_matrix)

# original Matrix : 
#  [[1 2 3]
#  [4 5 6]
#  [7 8 9]]
# transpose:
#  [[1 4 7]
#  [2 5 8]
#  [3 6 9]]