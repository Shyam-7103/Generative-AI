import pandas as pd

df = pd.read_csv("students.csv")

print(df.head())

print(df.shape)
print(df.columns)
print(df.tail())
print(df.info())  

print(df["Age"])
print(df["Age"].value_counts())

print(df["City"].value_counts())

