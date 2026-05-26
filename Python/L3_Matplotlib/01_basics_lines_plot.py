import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 15, 25]

# plt.plot(x, y)
# plt.plot(x, y, color="red", marker="o", linestyle="--")

# print(plt.xlabel("X-AXIS values"))
# print(plt.ylabel("Y-Axis values"))

# print(plt.title("Simple Line Plot"))

# print(plt.show())

# ------------------------------------------

# Practice

a = [1, 2, 3, 4, 5]
b = [2, 4, 6, 8, 10]

plt.plot(a, b, color="Blue", marker="o")
plt.plot(x, y)

plt.title("Market plot")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")

plt.show()
