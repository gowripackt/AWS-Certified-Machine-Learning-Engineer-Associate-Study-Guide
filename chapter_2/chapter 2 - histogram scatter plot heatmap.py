import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


# Generate a sample dataset with outliers and skewness
np.random.seed(42)

# Base data
customer_count = 100
ages = np.random.randint(18, 70, size=customer_count)
genders = np.random.choice(["Male", "Female"], size=customer_count)

# Create spending data with skewness
spending = np.random.gamma(2, 150, size=customer_count)  # Skewed distribution

# Add outliers to spending
outliers = np.array([2000, 2500, 3000])  # Extreme high spenders
spending_with_outliers = np.append(spending, outliers)
ages_with_outliers = np.append(ages, [30, 45, 50])  # Assign arbitrary ages for outliers
genders_with_outliers = np.append(genders, ["Male", "Female", "Male"])  # Assign genders

# Create a DataFrame
data = {
    "CustomerID": range(1, len(spending_with_outliers) + 1),
    "Age": ages_with_outliers,
    "Gender": genders_with_outliers,
    "Spending": spending_with_outliers,
}
df = pd.DataFrame(data)

# Plot 1: Histogram of Spending
plt.figure(figsize=(6, 4))
plt.hist(df["Spending"], bins=10, color='skyblue', edgecolor='black')
plt.title("Histogram of Spending (With Outliers and Skewness)")
plt.xlabel("Spending ($)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# Plot 2: Scatter Plot of Age vs Spending
plt.figure(figsize=(6, 4))
plt.scatter(df["Age"], df["Spending"], alpha=0.7, color='orange', edgecolor='black')
plt.title("Scatter Plot of Age vs Spending (With Outliers)")
plt.xlabel("Age (Years)")
plt.ylabel("Spending ($)")
plt.tight_layout()
plt.show()

# Plot 3: Box Plot of Spending by Gender
plt.figure(figsize=(6, 4))
df.boxplot(column="Spending", by="Gender", grid=False, patch_artist=True)
plt.title("Box Plot of Spending by Gender (With Outliers)")
plt.suptitle("")  # Remove the default title added by boxplot
plt.xlabel("Gender")
plt.ylabel("Spending ($)")
plt.tight_layout()
plt.show()


# Create a correlation heatmap for the dataset
# Adjust dataset to exclude 'CustomerID' and 'Region' for the heatmap
df_filtered = df.drop(columns=["CustomerID"])

# Encode categorical data for heatmap
df_filtered["Gender"] = df_filtered["Gender"].map({"Male": 0, "Female": 1})

# Compute correlation matrix
correlation_matrix = df_filtered.corr()

# Plot heatmap
plt.figure(figsize=(6, 4))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Correlation Heatmap (Excluding CustomerID)")
plt.tight_layout()
plt.show()