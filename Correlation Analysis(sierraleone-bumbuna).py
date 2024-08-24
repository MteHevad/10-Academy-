# Perform correlation analysis using a heatmap
plt.figure(figsize=(12, 10))

# Calculate the correlation matrix
correlation_matrix = df[['GHI', 'DNI', 'DHI', 'ModA', 'ModB', 'Tamb', 'RH', 'WS', 'WSgust', 'WD']].corr()

# Plot the heatmap
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')

# Set plot title
plt.title('Correlation Heatmap of Solar Radiation and Weather Variables')

# Show the plot
plt.show()
