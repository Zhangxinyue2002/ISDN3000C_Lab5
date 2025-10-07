import numpy as np
import pandas as pd

# --- TODO: Complete the tasks listed in tutorial. Run and verify your results before submission. --- #

'''
Load the datasets
'''
df = pd.read_csv('plant_sensors.csv')
'''
Exercise 1.1: Array Basics
'''
moisture_readings = pd.read_csv('plant_sensors.csv', usecols=['soil_moisture']).values
calibrated_moisture = moisture_readings - 0.5 # Example calibration offset
print(calibrated_moisture)     
'''
Exercise 1.2: Array Slicing and Stats
'''
print("Index 50-59 is:", '\n', moisture_readings[50:60])  # Slicing rows 50 to 59
print("Mean =", np.nanmean(moisture_readings))  # Mean of values
print("Median =", np.nanmedian(moisture_readings))   # Median of values
print("Std Dev =", np.nanstd(moisture_readings))  # Standard deviation of values
print("75th Percentile =", np.nanquantile(moisture_readings, 0.75))  # 75th percentile of values
'''
Exercise 1.3: Boolean Indexing and Logic
'''
Boolean_mask = (calibrated_moisture < 35) & ~np.isnan(calibrated_moisture)  # Create a boolean mask for values < 35
dry_readings = calibrated_moisture[Boolean_mask]
print("Number of dry readings:", dry_readings.size)  # Count of dry readings

#test
#print(calibrated_moisture[0:10])  # Print first 10 calibrated readings

moisture_status = np.where(calibrated_moisture < 35, 'Dry', np.where(calibrated_moisture > 70, 'Wet', 'OK'))  # Classify readings as 'Dry' or 'Wet' and 'OK'
print(moisture_status[0:10])  # Print the status array