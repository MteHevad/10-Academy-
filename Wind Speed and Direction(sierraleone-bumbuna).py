import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy import stats

# Wind analysis using polar plot
plt.figure(figsize=(10, 10))
ax = plt.subplot(111, projection='polar')
ax.scatter(np.radians(df['WD']), df['WS'], alpha=0.5)
ax.set_theta_zero_location('N')
ax.set_theta_direction(-1)
plt.title('Wind Speed and Direction')
plt.show()

# Temperature and humidity relationship
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Tamb', y='RH')
plt.title('Temperature vs Relative Humidity')
plt.xlabel('Ambient Temperature')
plt.ylabel('Relative Humidity')
plt.show()

# Distribution analysis with histograms
fig, axes = plt.subplots(2, 3, figsize=(15, 10))
sns.histplot(df['GHI'], kde=True, ax=axes[0, 0])
sns.histplot(df['DNI'], kde=True, ax=axes[0, 1])
sns.histplot(df['DHI'], kde=True, ax=axes[0, 2])
sns.histplot(df['WS'], kde=True, ax=axes[1, 0])
sns.histplot(df['Tamb'], kde=True, ax=axes[1, 1])
sns.histplot(df['RH'], kde=True, ax=axes[1, 2])
plt.tight_layout()
plt.show()

# Z-score analysis for outliers
z_scores = stats.zscore(df[['GHI', 'DNI', 'DHI', 'WS', 'Tamb', 'RH']])
outliers = (np.abs(z_scores) > 3).any(axis=1)
print(f"Number of outliers detected: {outliers.sum()}")
print(f"Percentage of outliers: {outliers.sum() / len(df) * 100:.2f}%")
