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

soil_moisture: 

---

## Question 3: What is the difference between the mean and median moisture reading? Given the system's purpose, why might you expect these values to differ?

**Answer:** 

---

## Question 4: After converting the timestamp column, what methods are now available on df['timestamp'].dt?

**Answer:**

---

## Question 5: Justify the reason behind your choice.

**Answer:**

---

## Question 6: Which sensor is in the driest environment on average? Which plant type requires the most water?

**Answer:**

---

## Question 7: Looking at your line plot, describe the daily pattern of soil moisture. What does it tell you about the environment and the watering system?

**Answer:**

---

## Question 8: What does the histogram tell you about the temperature environment? Based on the scatter plot, what is the general relationship between temperature and soil moisture?

**Answer:**

**Histogram Analysis:**

**Scatter Plot Analysis:**

---

## Final Challenge: 

**Visualizations**

**A short paragraph justifying which sensor you believe is faulty**
