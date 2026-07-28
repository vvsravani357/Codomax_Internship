# DAY 8 - DATA VISUALIZATION USING MATPLOTLIB

import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("D:/example/insurance.csv")

print("Dataset Loaded Successfully!")

# 1. BAR CHART

region_counts = df["region"].value_counts()

plt.figure(figsize=(6,4))
plt.bar(region_counts.index, region_counts.values)

plt.title("Number of People in Each Region")
plt.xlabel("Region")
plt.ylabel("Count")

plt.show()


# 2. LINE CHART


age_sorted = df.sort_values("age")

plt.figure(figsize=(8,5))
plt.plot(age_sorted["age"], age_sorted["charges"])

plt.title("Age vs Insurance Charges")
plt.xlabel("Age")
plt.ylabel("Charges")

plt.show()



# 3. PIE CHART


sex_counts = df["sex"].value_counts()

plt.figure(figsize=(6,6))
plt.pie(
    sex_counts.values,
    labels=sex_counts.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Gender Distribution")

plt.show()

print("All Charts Created Successfully!")