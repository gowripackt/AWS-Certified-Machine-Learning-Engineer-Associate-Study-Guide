import matplotlib.pyplot as plt

# Simulate data access times (in milliseconds) for row-based and column-based formats
query_types = ['Read Single Row', 'Read Single Column', 'Read Multiple Rows', 'Read Multiple Columns']
row_based_performance = [5, 15, 25, 30]  # Time taken for row-based access
column_based_performance = [20, 5, 35, 10]  # Time taken for column-based access

# Create a bar plot
x = range(len(query_types))
width = 0.35  # Width of the bars

plt.figure(figsize=(10, 6))

# Plot row-based performance
plt.bar(x, row_based_performance, width, label='Row-Based', color='skyblue')

# Plot column-based performance
plt.bar([p + width for p in x], column_based_performance, width, label='Column-Based', color='orange')

# Add labels and title
plt.xticks([p + width / 2 for p in x], query_types, rotation=45, ha='right')
plt.ylabel('Query Time (ms)')
plt.title('Query Performance: Row-Based vs. Column-Based Formats')
plt.legend()

# Show gridlines for clarity
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Display the plot
plt.tight_layout()
plt.show()