import numpy as np
# Changing the shape of the array without changing data

# a = np.array([0, 1, 2, 3, 4, 5, 6, 7])

# print(a.shape)

# b = a.reshape(2, 5)

# c = a.reshape(4, -1)

# print(c)
# print(c.shape)

# Broadcasting ---------------------------------------------------------

# b = np.array([0, 1, 2, 3, 4, 5, 6, 7])

# print(b * 2)

# c = np.array([[2, 3, 4], [5, 6, 7]])

# d = np.array([10, 20, 30])

# print(c + d)

# Practice --------------------------------------------------------------

e = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# print(e.shape)
# x = e.reshape(3, 4)
# print(x)

# y = e.reshape(2, -1)
# print(y)

f = np.array([1, 2, 3, 4])

print(f + 10)