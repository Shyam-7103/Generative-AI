import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

X = np.array([[1], [2], [3], [4], [5], [6]])
y = np.array([0, 0 ,0, 1, 1, 1])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LogisticRegression()

model.fit(X_train, y_train)

pred = model.predict(X_test)

print(pred)

print(model.predict([[2.5]]))

accuracy = accuracy_score(y_test, pred)

print("Accuracy", accuracy)