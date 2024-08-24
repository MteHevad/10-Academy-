import matplotlib.pyplot as plt

plt.figure(figsize=(12, 8))

scatter = plt.scatter(df['GHI'], df['Tamb'], s=df['WS']*10, c=df['RH'], cmap='viridis', alpha=0.6)

plt.xlabel('Global Horizontal Irradiance (GHI)')
plt.ylabel('Ambient Temperature (Tamb)')
plt.title('Bubble Chart: GHI vs Tamb vs WS (size) vs RH (color)')

plt.colorbar(scatter, label='Relative Humidity (RH)')

plt.tight_layout()
plt.show(
