# Perform time series analysis by plotting line graphs for GHI, DNI, DHI, and Tamb over time
import matplotlib.pyplot as plt
import seaborn as sns

# Set the figure size
plt.figure(figsize=(14, 8))

# Plot GHI, DNI, DHI, and Tamb over time
sns.lineplot(data=df, x='Timestamp', y='GHI', label='GHI')
sns.lineplot(data=df, x='Timestamp', y='DNI', label='DNI')
sns.lineplot(data=df, x='Timestamp', y='DHI', label='DHI')
sns.lineplot(data=df, x='Timestamp', y='Tamb', label='Tamb')

# Set plot title and labels
plt.title('Time Series Analysis of Solar Radiation and Temperature')
plt.xlabel('Timestamp')
plt.ylabel('Values')
plt.xticks(rotation=45)
plt.legend()

# Show the plot
plt.tight_layout()
plt.show()
