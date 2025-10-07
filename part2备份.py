# --- TODO: Complete the tasks listed in tutorial. Run and verify your results before submission. --- #
'''
Import necessary libraries here
'''
import numpy as np
import pandas as pd     
'''
Load the datasets
'''
df = pd.read_csv('plant_sensors.csv')

'''
Exercise 2.1: Initial Inspection & Cleaning
'''
print(df.head())  # Display the first few rows of the dataframe
print(df.shape())  # Get summary statistics of the dataframe
print(df.info())  # Get a concise summary of the dataframe
df['timestamp'] = pd.to_datetime(df['timestamp'])
temperature_f = df['temperature_c'] * 9/5 + 32  # Convert Celsius to Fahrenheit

'''
Exercise 2.2: Missing Data & Filtering
'''



'''
Exercise 2.3: Grouping and Aggregation
'''