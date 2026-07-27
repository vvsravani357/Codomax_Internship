# DAY 7 - DATA ANALYSIS

import pandas as pd

print("DAY 7 - DATA ANALYSIS")

# Load dataset
df = pd.read_csv("D:/example/insurance.csv")

# Display first 5 rows
print("\nFirst 5 Rows")
print(df.head())

# Select numerical columns
numerical_columns = df.select_dtypes(include=["number"])

print("\n DATA ANALYSIS ")

# Total
print("\n1. Total Values")
print(numerical_columns.sum())

# Average
print("\n2. Average Values")
print(numerical_columns.mean())

# Minimum
print("\n3. Minimum Values")
print(numerical_columns.min())

# Maximum
print("\n4. Maximum Values")
print(numerical_columns.max())

# Count
print("\n5. Count Values")
print(numerical_columns.count())

print("\n BASIC BUSINESS INSIGHTS ")

print(f"Average Age: {df['age'].mean():.2f} years")
print(f"Average BMI: {df['bmi'].mean():.2f}")
print(f"Average Children: {df['children'].mean():.2f}")
print(f"Average Insurance Charges: ${df['charges'].mean():.2f}")

print(f"\nHighest Insurance Charge: ${df['charges'].max():.2f}")
print(f"Lowest Insurance Charge: ${df['charges'].min():.2f}")

print(f"\nTotal Customers: {df['charges'].count()}")

print("\nAnalysis Completed Successfully!")