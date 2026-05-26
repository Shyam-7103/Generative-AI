import matplotlib.pyplot as plt
import pandas as pd

x = [1, 2, 3, 4]
y1 = [10, 20, 30, 40]
y2 = [5, 15, 25, 35]

# plt.subplot(1, 2, 1)
# plt.plot(x, y1)
# plt.title("Plot 1")

# plt.subplot(1, 2, 2)
# plt.plot(x, y2)
# plt.title("Plot 2")

# plt.show()

# -----------------------------------------

# data = {
#     "Year":[2020,2021,2022,2023],
#     "Sales":[100,150,200,250]
# }

# df = pd.DataFrame(data)

# df.plot(x="Year", y="Sales", kind="line")

# plt.show()

# ---------------------------------------------

data = {
    "Year":[2020,2021,2022],
    "Sales":[100,150,200],
    "Profit":[20,40,60]
}

df = pd.DataFrame(data)

df.plot(x="Year")

plt.show()

