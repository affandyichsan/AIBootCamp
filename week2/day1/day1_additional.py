# crete 4x4 matrix and calculation the sum of its rows and colums
# write a program to normalize an array (scale values between 0 and 1)
# Generate a random array and find the minimum and maximum values
import numpy as np
# crete 4x4 matrix and calculation the sum of its rows and colums
arr = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
# Generate a random array and find the minimum and maximum values
arr2 = np.random.randint(0, 100, size=10)
min_val = np.min(arr2)
max_val = np.max(arr2)
# write a program to normalize an array (scale values between 0 and 1)

normalized_array = (arr2 - min_val)/(max_val -min_val)

print(sum(arr))
print(arr[:1])
print("original array : ", arr2)

print("min :", min_val)
print("max :", max_val)

print("normalized array :",normalized_array)