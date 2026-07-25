# Day 5 - Data Cleaning using Pandas

import pandas as pd

print("DAY 5 - DATA CLEANING")

# Load Dataset
df = pd.read_csv("insurance.csv")

print("\nOriginal Dataset")
print(df.head())

# 1. Check Missing Values

print("\n1. Missing Values")
print(df.isnull().sum())

# Fill missing values (if any)
# Numerical columns -> Mean
# Categorical columns -> Mode

for column in df.columns:
    if df[column].dtype == "object":
        df[column] = df[column].fillna(df[column].mode()[0])
    else:
        df[column] = df[column].fillna(df[column].mean())

print("\nMissing Values After Cleaning")
print(df.isnull().sum())

# 2. Check Duplicate Records

print("\n2. Duplicate Records")

duplicates = df.duplicated().sum()
print("Duplicate Rows:", duplicates)

# Remove duplicates
df = df.drop_duplicates()

print("Duplicate Rows After Removing:", df.duplicated().sum())

# 3. Check Data Types

print("\n3. Data Types Before Correction")
print(df.dtypes)

# Convert data types if required

df["age"] = df["age"].astype(int)
df["children"] = df["children"].astype(int)

print("\nData Types After Correction")
print(df.dtypes)

# 4. Dataset Information

print("\nDataset Information")
print(df.info())

# 5. Save Clean Dataset

df.to_csv("insurance_cleaned.csv", index=False)

print("\nClean dataset saved successfully!")
print("File Name: insurance_cleaned.csv")

print("\nFirst 5 Rows of Clean Dataset")
print(df.head())
