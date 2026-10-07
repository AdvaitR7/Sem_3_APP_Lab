import pandas as pd
import numpy as np

print("Student Name: Advait R")

# Step 1: Create a Pandas Series with 10 random numbers
data = np.random.randint(1, 100, 10)
series = pd.Series(data)

print("\nSeries of 10 Random Numbers:")
print(series)

# Step 2: Indexing
print("\nAccessing element at index 3:", series.iloc[3])
print("Accessing first 5 elements:")
print(series.iloc[:5])

# Step 3: Filtering
print("\nFiltering numbers greater than 50:")
print(series[series > 50])

# Step 4: Statistical Operations
print("\nStatistical Operations:")
print("Mean   :", series.mean())
print("Median :", series.median())
print("Minimum:", series.min())
print("Maximum:", series.max())