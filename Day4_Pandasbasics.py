import pandas as pd

print("DAY 4 - PANDAS BASICS")
# Load CSV Dataset
df = pd.read_csv("insurance.csv")

# First 5 rows
print("\n1. First 5 Rows")
print(df.head())

# Last 5 rows
print("\n2. Last 5 Rows")
print(df.tail())

# Column names
print("\n3. Column Names")
print(df.columns.tolist())

# Dataset information
print("\n4. Dataset Information")
df.info()

# Dataset shape
print("\n5. Dataset Shape")
print(df.shape)

# Statistical summary
print("\n6. Statistical Summary")
print(df.describe())
