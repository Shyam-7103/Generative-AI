import numpy as np

a = np.array([[1, 2, 3], 
              [4, 5, 6 ]])

# print(a)
# print(a.T)

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

# print(np.dot(x, y))
# print(x @ y)  # Modern Way
# will multiply same as row wise and then add it

b = np.array([0, 1, 2, 3, 4, 5, 6])

# print(b > 2)
# print(b[b > 2])

# a[a > 30] = 999
# print(a)

# Practice --------------------------------------------------

s = np.array([[3, 4, 5], 
             [30, 40, 50]])

h = np.array([2, 3])
m = np.array([5, 6])

# print(s.T)

# print(np.dot(h, m))

# print(h * m)

# Masking

p = np.array([5, 10, 15, 20, 25])

# print(p[p > 12])

# print(p[(p > 10) & (p <25)])

p[p < 15] = 0
print(p)