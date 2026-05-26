import pandas as pd

# a = pd.Series([10, 20, 30, 40])

# print(a)

# b = pd.Series([50, 60, 70, 80], index=["a", 'b', 'c', 'd'])

# print(b)

data = {
    "Name" : ["Aditya", "Shakti", "Miren"],
    "Age"  : [22, 23, 30],
    "Salary" : [10000, 15000, 20000]
}

df = pd.DataFrame(data)

# print(df)
# print(df.shape)
# print(df.columns)
# print(df.head())
# print(df[["Age", "Salary"]])

# Practice ---------------------------------

data1 = {
    "Name" : ["A", "B", "C"],
    "Marks" : [85, 90, 78],
    "City" : ["Delhi", "Mumbai", "Pune"]
}

df1 = pd.DataFrame(data1)
# print(df1)

# print(df1.shape)
# print(df1[0:2])
# print(df1["Marks"])
print(df1[["Name", "City"]])
