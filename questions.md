# Lab 05: Answer Sheet

## Question 1: How many rows were generated? How many were expected? Why?

**Answer:** 
3606 rows were generated including 1 row of title.
Total hours should be from 00:00 1st Jul to 23:00 31st Jul (744hr), total row = 744 * 5 = 3720.

However when I print the time_range, it shows:
DatetimeIndex(['2023-07-01 00:00:00', '2023-07-01 01:00:00',
               '2023-07-01 02:00:00', '2023-07-01 03:00:00',
               '2023-07-01 04:00:00', '2023-07-01 05:00:00',
               '2023-07-01 06:00:00', '2023-07-01 07:00:00',
               '2023-07-01 08:00:00', '2023-07-01 09:00:00',
               ...
               '2023-07-30 15:00:00', '2023-07-30 16:00:00',
               '2023-07-30 17:00:00', '2023-07-30 18:00:00',
               '2023-07-30 19:00:00', '2023-07-30 20:00:00',
               '2023-07-30 21:00:00', '2023-07-30 22:00:00',
               '2023-07-30 23:00:00', '2023-07-31 00:00:00'],
              dtype='datetime64[ns]', length=721, freq='h')

The hours is 721, so 721 * 5 = 3605 rows (Plus 1 row of title)
---

## Question 2: What appears to be the unit of temperature, soil_moisture, and light_level?

**Answer:**
Temperature: the variable called temp_c and temperature_c so should be Celsius (°C), also from the plant_sensors.csv, the temperature is in a range of 15 - 30, so reseasonable to be °C.

soil_moisture: percentage %

light_level : lux

---

## Question 3: What is the difference between the mean and median moisture reading? Given the system's purpose, why might you expect these values to differ?

**Answer:** 
Outliers: 
The mean can be heavily influenced by extreme values (outliers) that may be present in the data. If there are a few very high moisture readings, they will pull the mean up, while the median remains unaffected, as it is the middle value.

Data Distribution: 
The data distribution could be skewed. If the moisture readings have a right skew (where most readings are on the lower end, with some higher readings), this could lead to a situation where the mean is higher than the median.
---

## Question 4: After converting the timestamp column, what methods are now available on df['timestamp'].dt?

**Answer:**
.dt.year
.dt.month
.dt.day
.dt.hour
.dt.minute
.dt.second
.dt.weekday
---

## Question 5: Justify the reason behind your choice.

**Answer:**
Soil moisture: Used linear interpolation because soil moisture changes gradually over time, making interpolation appropriate for filling gaps between known values
Timestamp, sensor_id, plant_type, location: Dropped rows with missing values because these are categorical identifiers that cannot be meaningfully interpolated
Temperature and light_level: Used forward fill then backward fill because these environmental variables change gradually and nearby values are good approximations
These choices preserve data integrity while maintaining realistic relationships between variables.
---

## Question 6: Which sensor is in the driest environment on average? Which plant type requires the most water?

**Answer:**
*Driest sensor*: B-2 (Pothos in Office) with average soil moisture of 39.09%
*Plant requiring most water*: Tomato with 228 pump activations

This makes biological sense as tomatoes are water-intensive plants, especially when grown in sunny outdoor conditions (Patio location), while office plants typically have more stable, controlled environments.

---

## Question 7: Looking at your line plot, describe the daily pattern of soil moisture. What does it tell you about the environment and the watering system?

**Answer:**
The line plot shows a cyclical daily pattern where soil moisture decreases during daylight hours and recovers at night. This indicates:

Environment: Higher temperatures and light levels during the day increase evaporation and plant water uptake
Watering system: The automated system successfully maintains moisture levels by activating pumps when moisture drops below the 35% threshold
Natural cycles: The saw-tooth pattern shows the system working as designed - moisture drops during stress periods and recovers through automated watering

---

## Question 8: What does the histogram tell you about the temperature environment? Based on the scatter plot, what is the general relationship between temperature and soil moisture?

**Answer:**

**Histogram Analysis:**
 The temperature histogram shows a bimodal distribution with two distinct peaks - one around 16°C and another around 24°C, with a dip around 20°C. This indicates a clear daily temperature cycle where temperatures are cooler during night/early morning hours and warmer during daytime, which is typical for indoor environments with natural temperature fluctuations.
**Scatter Plot Analysis:**
The scatter plot reveals a negative correlation between temperature and soil moisture - as temperature increases, soil moisture tends to decrease. This is expected because higher temperatures increase evaporation rates and plant water uptake. There are some outlier points (likely from sensor B-1) that show unusually high moisture values regardless of temperature, indicating sensor malfunction.
---

## Final Challenge: 

**Visualizations**

**A short paragraph justifying which sensor you believe is faulty**
