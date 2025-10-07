# --- TODO: Complete the tasks listed in tutorial. Run and verify your results before submission. --- #
'''
Import necessary libraries here
'''
import pandas as pd
import numpy as np

'''
Load the datasets
'''
print("Dataset:")
df = pd.read_csv('plant_sensors.csv')

'''
Exercise 2.1: Initial Inspection & Cleaning
'''

print("First 5 rows:")
print(df.head())
print("Dataset shape:")
print(df.shape)
print("Dataset info:")
print(df.info())


#print(df['timestamp'].dtype)
df['timestamp'] = pd.to_datetime(df['timestamp'])
print(df['timestamp'].dtype)

df['temperature_f'] = (df['temperature_c'] * 9/5) + 32


#print(df['timestamp'].dt.hour.head())
#print(df['timestamp'].dt.dayofweek.head())
#print(df['timestamp'].dt.month.head())
#print(df['timestamp'].dt.year.head())


'''
Exercise 2.2: Missing Data & Filtering
'''

print("Missing values:")
missing_values = df.isnull().sum()
print(missing_values)

df['soil_moisture'] = df['soil_moisture'].interpolate(method='linear', limit_direction='both')
df = df.dropna(subset=['timestamp', 'sensor_id', 'plant_type', 'location'])
df['temperature_c'] = df['temperature_c'].ffill().bfill()
df['light_level'] = df['light_level'].ffill().bfill()

print("Missing values after cleaning:")
print(df.isnull().sum())

patio_high_light = df[(df['location'] == 'Patio') & (df['light_level'] > 1200)]
print("Number of records:")
print(len(patio_high_light))
print("First 5 rows:")
print(patio_high_light.head())

'''
Exercise 2.3: Grouping and Aggregation
'''
avg_moisture_by_sensor = df.groupby('sensor_id')['soil_moisture'].mean()
print("Average soil moisture by sensor:")
print(avg_moisture_by_sensor)

pump_activations_by_plant = df.groupby('plant_type')['pump_active'].sum()
print("Total number of times the pump was activated:")
print(pump_activations_by_plant)

max_temp_by_location = df.groupby('location')['temperature_c'].max()
print("Maximum temperature by location:")
print(max_temp_by_location)


print("Summary:")
driest_sensor = avg_moisture_by_sensor.idxmin()
lowest_moisture = avg_moisture_by_sensor.min()
print("Driest sensor:")
print(driest_sensor)
print("Lowest moisture:")
print(lowest_moisture)

most_water_plant = pump_activations_by_plant.idxmax()
most_activations = pump_activations_by_plant.max()
print("Plant type requiring most water:")
print(most_water_plant)
print("Most activations:")
print(most_activations)
