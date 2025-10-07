# --- TODO: Complete the tasks listed in tutorial. Run and verify your results before submission. --- #
'''
Import necessary libraries here
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
'''
Load the datasets
'''
df = pd.read_csv('plant_sensors.csv')


df['timestamp'] = pd.to_datetime(df['timestamp'])
df['temperature_f'] = (df['temperature_c'] * 9/5) + 32
df['soil_moisture'] = df['soil_moisture'].interpolate(method='linear', limit_direction='both')
df = df.dropna(subset=['timestamp', 'sensor_id', 'plant_type', 'location'])
df['temperature_c'] = df['temperature_c'].ffill().bfill()
df['light_level'] = df['light_level'].ffill().bfill()
df['temperature_f'] = (df['temperature_c'] * 9/5) + 32

'''
Exercise 3.1: Bar Chart
'''
print("Bar Chart:")

avg_moisture_by_sensor = df.groupby('sensor_id')['soil_moisture'].mean()

plt.figure(figsize=(10, 6))
bars = plt.bar(avg_moisture_by_sensor.index, avg_moisture_by_sensor.values, 
               color=['#2E8B57', '#4682B4', '#DC143C', '#FF8C00', '#9932CC'])

# Customize the plot
plt.title('Average Soil Moisture by Sensor', fontsize=16, fontweight='bold')
plt.ylabel('Average Moisture (%)', fontsize=12)
plt.xlabel('Sensor ID', fontsize=12)
plt.ylim(0, max(avg_moisture_by_sensor.values) * 1.1)

# Add value labels on bars
for bar, value in zip(bars, avg_moisture_by_sensor.values):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5, 
             f'{value:.1f}%', ha='center', va='bottom', fontweight='bold')

plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('average_moisture_by_sensor.png', dpi=300, bbox_inches='tight')
plt.show()

'''
Exercise 3.2: Line Plot
'''
print("\n=== Exercise 3.2: Line Plot ===")

# Filter data for sensor A-1 (has full month data) and set timestamp as index
sensor_a1 = df[df['sensor_id'] == 'A-1'].copy()
sensor_a1 = sensor_a1.set_index('timestamp')

# Create line plot with reduced detail for full month view
plt.figure(figsize=(15, 6))
plt.plot(sensor_a1.index, sensor_a1['soil_moisture'], linewidth=0.8, color='#1E90FF', alpha=0.7)

plt.title('Moisture Level for Sensor A-1 (Full Month)', fontsize=16, fontweight='bold')
plt.xlabel('Time', fontsize=12)
plt.ylabel('Soil Moisture (%)', fontsize=12)
plt.grid(True, alpha=0.3)

# Format x-axis to show all dates across the month
ax = plt.gca()
# Show every 2 days to cover full month without overcrowding
ax.xaxis.set_major_locator(mdates.DayLocator(interval=2))  # Every 2 days
ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))  # Format as MM-DD
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('moisture_timeline_A1.png', dpi=300, bbox_inches='tight')
plt.show()

'''
Exercise 3.3: Subplots and Anomaly Detection
'''
print("\n=== Exercise 3.3: Subplots and Anomaly Detection ===")

# Create figure with subplots
fig, axes = plt.subplots(1, 2, figsize=(15, 6))

# Left subplot: Temperature histogram
axes[0].hist(df['temperature_c'], bins=40, color='coral', alpha=0.7, edgecolor='black')
axes[0].set_title('Distribution of All Temperature Readings', fontsize=14, fontweight='bold')
axes[0].set_xlabel('Temperature (°C)', fontsize=12)
axes[0].set_ylabel('Frequency', fontsize=12)
axes[0].grid(axis='y', alpha=0.3)

# Right subplot: Temperature vs Soil Moisture scatter plot
scatter = axes[1].scatter(df['temperature_c'], df['soil_moisture'], 
                         alpha=0.1, c='blue', s=10)
axes[1].set_title('Temperature vs. Soil Moisture', fontsize=14, fontweight='bold')
axes[1].set_xlabel('Temperature (°C)', fontsize=12)
axes[1].set_ylabel('Soil Moisture (%)', fontsize=12)
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('temperature_analysis.png', dpi=300, bbox_inches='tight')
plt.show()

# Additional analysis for anomaly detection
print("\n=== Additional Analysis for Anomaly Detection ===")

# Analyze each sensor's behavior
print("Sensor behavior analysis:")
sensor_stats = df.groupby('sensor_id').agg({
    'soil_moisture': ['mean', 'std', 'min', 'max', 'count'],
    'temperature_c': ['mean', 'std'],
    'pump_active': 'sum'
}).round(2)

print(sensor_stats)

# Look for outliers in soil moisture
plt.figure(figsize=(12, 8))

# Create a box plot for each sensor
sensors = df['sensor_id'].unique()
moisture_data = [df[df['sensor_id'] == sensor]['soil_moisture'].values for sensor in sensors]

box_plot = plt.boxplot(moisture_data, labels=sensors, patch_artist=True)

# Color the boxes
colors = ['#2E8B57', '#4682B4', '#DC143C', '#FF8C00', '#9932CC']
for patch, color in zip(box_plot['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)

plt.title('Soil Moisture Distribution by Sensor (Box Plot)', fontsize=16, fontweight='bold')
plt.xlabel('Sensor ID', fontsize=12)
plt.ylabel('Soil Moisture (%)', fontsize=12)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('moisture_boxplot_by_sensor.png', dpi=300, bbox_inches='tight')
plt.show()

print("\nExercise 3 completed successfully!")