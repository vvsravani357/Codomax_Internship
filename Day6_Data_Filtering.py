

# Import Pandas
import pandas as pd

print("DAY 6 - DATA FILTERING")

# Load Dataset
df = pd.read_csv("D:/example/insurance.csv")

# Display first 5 rows
print("\nOriginal Dataset")
print(df.head())

# 1. Select Columns

print("\nSelected Columns (Age, BMI, Charges)")
selected_columns = df[['age', 'bmi', 'charges']]
print(selected_columns.head())

# 2. Filter Rows
# Example: People older than 30

print("\nPeople with Age > 30")
age_filter = df[df['age'] > 30]
print(age_filter.head())


# Another Filter
# Smokers only

print("\nSmokers Only")
smokers = df[df['smoker'] == 'yes']
print(smokers.head())


# 3. Multiple Conditions
# Age > 30 and BMI > 30

print("\nAge > 30 and BMI > 30")
multiple_filter = df[(df['age'] > 30) & (df['bmi'] > 30)]
print(multiple_filter.head())


# 4. Sort Dataset

print("\nSorted by Charges (Highest First)")
sorted_df = df.sort_values(by='charges', ascending=False)
print(sorted_df.head())


# Save Filtered Dataset

multiple_filter.to_csv("insurance_filtered.csv", index=False)

print("\nFiltered dataset saved as insurance_filtered.csv")