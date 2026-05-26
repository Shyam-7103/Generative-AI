import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


X = np.array([[1], [2], [3], [4], [5], [6]])
# Experince

y = np.array([30000, 35000, 40000, 45000, 50000, 55000])
# Salary

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()

model.fit(X_train, y_train)

predict = model.predict(X_test)

# print(predict)

error = mean_squared_error(y_test, predict)

# print("Error", error)

# print(X_train)
# print(X_test)
# print(y_train)
# print(y_test)
# print(predict)
# print(model.predict([[7]]))


# Dataset
# Train/Test Split
# Train model
# Prediction
# Evaluation