# DAY 9 - MINI DASHBOARD
# Data Analytics Internship


# Import Libraries
import pandas as pd
import matplotlib.pyplot as plt


print("      DAY 9 - MINI DASHBOARD")

# Load Dataset

df = pd.read_csv("online_shoppers_intention.csv")

# Dataset Overview

print("\n1. First 5 Rows")
print(df.head())

print("\n2. Dataset Shape")
print(df.shape)

print("\n3. Dataset Information")
print(df.info())

print("\n4. Missing Values")
print(df.isnull().sum())

print("\n5. Statistical Summary")
print(df.describe())

# Dashboard Statistics

print("DASHBOARD SUMMARY")

print(f"Total Records : {len(df)}")
print(f"Total Features : {len(df.columns)}")

print(f"\nAverage Administrative Pages : {df['Administrative'].mean():.2f}")
print(f"Average Product Pages : {df['ProductRelated'].mean():.2f}")
print(f"Average Bounce Rate : {df['BounceRates'].mean():.4f}")
print(f"Average Exit Rate : {df['ExitRates'].mean():.4f}")

print("\nVisitor Types")
print(df["VisitorType"].value_counts())

print("\nRevenue Distribution")
print(df["Revenue"].value_counts())


# Chart 1 - Visitors by Month

month_counts = df["Month"].value_counts().sort_index()

plt.figure(figsize=(8,5))
month_counts.plot(kind="bar")

plt.title("Visitors by Month")
plt.xlabel("Month")
plt.ylabel("Number of Visitors")

plt.tight_layout()
plt.show()


# Chart 2 - Revenue Distribution

revenue = df["Revenue"].value_counts()

plt.figure(figsize=(6,6))

plt.pie(
    revenue,
    labels=["No Purchase", "Purchase"],
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Revenue Distribution")

plt.tight_layout()
plt.show()


# Chart 3 - Product Pages by Visitor Type

visitor = df.groupby("VisitorType")["ProductRelated"].mean()

plt.figure(figsize=(8,5))
visitor.plot(kind="bar")

plt.title("Average Product Related Pages")
plt.xlabel("Visitor Type")
plt.ylabel("Average Product Pages")

plt.tight_layout()
plt.show()

# Chart 4 - Bounce Rate by Month

bounce = df.groupby("Month")["BounceRates"].mean()

plt.figure(figsize=(8,5))

plt.plot(
    bounce.index,
    bounce.values,
    marker="o"
)

plt.title("Average Bounce Rate by Month")
plt.xlabel("Month")
plt.ylabel("Bounce Rate")

plt.grid(True)

plt.tight_layout()
plt.show()

# Chart 5 - Revenue by Visitor Type

revenue_visitor = pd.crosstab(df["VisitorType"], df["Revenue"])

revenue_visitor.plot(
    kind="bar",
    figsize=(8,5)
)

plt.title("Revenue by Visitor Type")
plt.xlabel("Visitor Type")
plt.ylabel("Number of Visitors")

plt.tight_layout()
plt.show()

# Chart 6 - Weekend Visits

weekend = df["Weekend"].value_counts()

plt.figure(figsize=(6,6))

plt.pie(
    weekend,
    labels=["Weekday", "Weekend"],
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Weekend Visits")

plt.tight_layout()
plt.show()

print("\nDashboard Created Successfully!")
