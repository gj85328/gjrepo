
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/expenses.csv")
summary = df.groupby("category")["amount"].sum().sort_values(ascending=False)
print(summary)

summary.plot(kind="bar", title="Spending by Category")
plt.tight_layout()
plt.savefig("images/spending_by_category.png")
print("Saved chart -> images/spending_by_category.png")
