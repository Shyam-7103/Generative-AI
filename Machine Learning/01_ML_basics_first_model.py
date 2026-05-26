import numpy as np
from sklearn.linear_model import LinearRegression

# X = np.array([[1],[2],[3],[4]])
# y = np.array([30000,50000,70000,90000])

# model = LinearRegression()

# model.fit(X,y)

# predict = model.predict([[5]])

# print(predict)

# -----------------------------------
# Practice

experince = np.array([[1], [2], [3]])
salary = np.array([30000, 65000, 90000])

model = LinearRegression()

model.fit(experince, salary)

predict1 = model.predict([[4]])

print(predict1)

