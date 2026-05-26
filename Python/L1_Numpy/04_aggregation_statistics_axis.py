import numpy as np

a = np.array([10, 20, 30, 40, 50])

# print(np.min(a))
# print(np.max(a))
# print(np.sum(a))
# print(np.mean(a))  # imp
# print(np.std(a))   # imp
# print(np.var(a))

b = np.array([[10, 20, 30], [40, 50, 60]])

# print(np.sum(b, axis=0))
# print(np.sum(b, axis=1))

# print(np.mean(b, axis=0))
# print(np.mean(b, axis=1))

# Practice --------------------------------------------

c = np.array([[5, 10, 15],
              [20, 25, 30],
              [35, 40, 45]])

# print(np.sum(c))

# print(np.mean(c))

# print(np.sum(c, axis=0))

print(np.mean(c, axis=1))

# print(np.std(c))
