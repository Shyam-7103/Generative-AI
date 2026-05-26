import pandas as pd

df = pd.read_csv("students.csv")

# print(df.isnull()) # Gives True or False

# print(df.isnull().count())

# df.fillna(0)

# print(df.sort_values("Age"))

# print(df.sort_values(["Marks", "Age"]))

# print(df.groupby("City")["Age"].mean())

# ----------------------------------------

# Practice

# print(df.isnull())

# print(df.isna())

# print(df.isna().count())

# df["Age"].fillna(df["Age"].mean(), inplace=True)

# df = df.fillna(df.mean())

print(df)