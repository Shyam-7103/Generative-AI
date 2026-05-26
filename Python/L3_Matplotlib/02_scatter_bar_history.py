import matplotlib.pyplot as plt

age = [20, 22 ,25, 27, 30]
salary = [20000, 25000, 30000, 35000, 40000]

plt.scatter(age, salary)

plt.title("Age vs Salary")
plt.xlabel("Age")
plt.ylabel("Salary")

plt.show()

# cities = ["Delhi", "Mumbai", "Chennai", "Pune"]
# students = [50, 40, 30, 20]

# plt.bar(cities, students)

# plt.title("Cities vs Students")
# plt.xlabel("Cities")
# plt.ylabel("Students")

# plt.show()

# marks = [60, 73, 54, 55, 70, 75, 98, 92, 10]

# plt.hist(marks)

# plt.title("Marks Distribution")
# plt.xlabel("Marks")
# plt.ylabel("Frequency")

# plt.show()