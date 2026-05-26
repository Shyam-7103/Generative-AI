import pandas as pd

df = pd.read_csv("students.csv")

# print(df.loc[0, "Name"])

# print(df.iloc[0, 3])

# print(df["Marks"].apply(lambda x: x + 5))

df1 = pd.DataFrame({
    "ID": [1,2,3,4],
    "Name": ["A","B","C","D"]
})

df2 = pd.DataFrame({
    "ID": [1,2,3,5],
    "Salary": [50000,60000,70000,80000]
})

print(pd.merge(df1, df2, on="ID"))