import pandas as pd

# Load the dataset
df = pd.read_csv("online_shoppers_intention.csv")   # Replace with your file name if different

# Display dataset information
print("Dataset Information")
print(df.info())

# Display statistical summary
print("\nStatistical Summary")
print(df.describe())

# Display missing values
print("\nMissing Values")
print(df.isnull().sum())

# Export the dataset to a new CSV file
output_file = "online_shoppers_cleaned.csv"
df.to_csv(output_file, index=False)

print(f"\n✅ Cleaned dataset exported successfully as '{output_file}'")
