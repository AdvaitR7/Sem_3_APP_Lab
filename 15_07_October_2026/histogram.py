import matplotlib.pyplot as plt
import seaborn as sns

age = [18, 20, 21, 22, 23, 23, 24, 25, 27, 30, 32, 35, 40]
salary = [20000, 22000, 25000, 28000, 30000, 32000, 35000,
          38000, 42000, 45000, 50000, 55000, 65000]

# Matplotlib histogram
plt.hist(age, bins=5, edgecolor="black")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.title("Age Distribution")
plt.show()

# Seaborn histogram
sns.histplot(salary, bins=5, kde=True)
plt.xlabel("Salary")
plt.title("Salary Distribution")
plt.show()