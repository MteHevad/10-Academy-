# Calculate summary statistics for each numeric column
descriptive_stats = df.describe().T

# Add median to the statistics
descriptive_stats['median'] = df.median()

# Display the summary statistics
descriptive_stats
