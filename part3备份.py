import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Load the dataset
df = pd.read_csv('plant_sensors.csv')

# ---- Exercise 3.1: Bar Chart ----
# Calculate average soil moisture per sensor
avg_soil_moisture_per_sensor = df.groupby('sensor_id')['soil_moisture'].mean()

# Create a bar chart
plt.figure(figsize=(10, 5))
avg_soil_moisture_per_sensor.plot(kind='bar', color='skyblue')
plt.title('Average Soil Moisture by Sensor')
plt.xlabel('Sensor IDs')
plt.ylabel('Average Moisture (%)')
plt.xticks(rotation=45)  # Rotate sensor IDs for better readability
plt.tight_layout()  # Adjust layout to make room for the rotated labels
plt.show()

# ---- Exercise 3.2: Line Plot ----
# Filter DataFrame for a specific sensor (e.g., 'A-1') and set timestamp as index
sensor_data = df[df['sensor_id'] == 'A-1'].set_index('timestamp')

# Create a line plot for the soil moisture of this sensor
plt.figure(figsize=(12, 6))
plt.plot(sensor_data.index, sensor_data['soil_moisture'], color='orange', label='Soil Moisture')
plt.title('Moisture Level for Sensor A-1')
plt.xlabel('Timestamp')
plt.ylabel('Soil Moisture (%)')
plt.xticks(rotation=45)  # Rotate x-axis labels for better visibility
plt.legend()
plt.tight_layout()
plt.show()

# ---- Exercise 3.3: Subplots and Anomaly Detection ----
# Create two subplots arranged side-by-side
fig, axes = plt.subplots(1, 2, figsize=(15, 6))  # 1 row, 2 columns

# Left subplot: Histogram of temperature_c
axes[0].hist(df['temperature_c'].dropna(), bins=40, color='lightgreen', edgecolor='black')
axes[0].set_title('Distribution of All Temperature Readings')
axes[0].set_xlabel('Temperature (°C)')
axes[0].set_ylabel('Frequency')

# Right subplot: Scatter plot of temperature_c vs soil_moisture
axes[1].scatter(df['temperature_c'], df['soil_moisture'], alpha=0.1, color='blue')
axes[1].set_title('Temperature vs. Soil Moisture')
axes[1].set_xlabel('Temperature (°C)')
axes[1].set_ylabel('Soil Moisture (%)')

# Display the plots
plt.tight_layout()
plt.show()