import numpy as np

a = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])

# Locating single element through its index
# print(a[6])
# print(a[-6])

# Slicing 1D array 
# print(a[1:5])
# print(a[1:8:2])

 
b = np.array([[1, 2, 3], [4, 5, 6]])

# Indexing 2D array
# print(b[1][1])
# print(b[1, 1])

# Slicing 2D Array
# print(b[1:2, 0:2])

# Entire row and column
# print(b[0, :])
# print(b[:, 0])

# b[1, 2] = 66
# print(b)

c = np.array([[10, 20, 30],
              [40, 50, 60],
              [70, 80, 90]])

# print(c[1,1])

# print(c[1, :])

print(c[:,2])

# print(c[1:3, 1:3])