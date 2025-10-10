# Lab 05: Answer Sheet

## Question 1: How many rows were generated? How many were expected? Why?

**Generated rows:** 3,606 rows (including 1 header row)

**Expected calculation:** 
- Time period: July 1-31, 2023 (00:00 to 23:00 on July 31)
- Expected hours: 744 hours
- Expected rows: 744 × 5 sensors = 3,720 rows

**Actual result:** 
The time_range shows 721 hours (from 2023-07-01 00:00:00 to 2023-07-31 00:00:00), resulting in:
- 721 × 5 sensors = 3,605 data rows + 1 header row = 3,606 total rows

---

## Question 2: What appears to be the unit of temperature, soil_moisture, and light_level?

**Temperature:** Celsius (°C)
- Variable names suggest Celsius (temp_c, temperature_c)
- Values range 15-30°C, which is reasonable for indoor plant environments

**Soil Moisture:** Percentage (%)

**Light Level:** Lux

---

## Question 3: What is the difference between the mean and median moisture reading? Given the system's purpose, why might you expect these values to differ?

**Reasons for difference:**

1. **Outliers:** Extreme moisture readings (Cause by broken B-1) can skew the mean while leaving the median unaffected
2. **System Purpose:** In a plant monitoring system, occasional sensor malfunctions or irrigation events can create outliers that affect the mean more than the median (Asked AI)

---

## Question 4: After converting the timestamp column, what methods are now available on df['timestamp'].dt? 

(We asked AI for this question)
**Available datetime accessor methods:**
- `.dt.year` - Extract year
- `.dt.month` - Extract month
- `.dt.day` - Extract day
- `.dt.hour` - Extract hour
- `.dt.minute` - Extract minute
- `.dt.second` - Extract second
- `.dt.weekday` - Extract day of week
---

## Question 5: Justify the reason behind your choice for handling missing data.

(We asked AI for this question TT)
**Data handling strategy:**

- **Soil moisture:** Linear interpolation
  - *Rationale:* Soil moisture changes gradually over time, making interpolation appropriate for filling gaps between known values

- **Categorical data** (timestamp, sensor_id, plant_type, location): Drop rows
  - *Rationale:* These are identifiers that cannot be meaningfully interpolated

- **Environmental variables** (temperature, light_level): Forward fill then backward fill
  - *Rationale:* Environmental conditions change gradually, and nearby temporal values provide good approximations (Asked AI)

---

## Question 6: Which sensor is in the driest environment on average? Which plant type requires the most water?

**Driest sensor:** B-2 (Average soil moisture: 39.09%)

**Plant requiring most water:** Tomato (Total pump activations: 228)

**Biological justification:** 
Tomatoes are water-intensive plants, especially in sunny outdoor conditions (Patio location). Office plants like Pothos typically have more stable, controlled environments with lower water requirements.(AI helped)

---

## Question 7: Looking at your line plot, describe the daily pattern of soil moisture. What does it tell you about the environment and the watering system?

**Daily pattern observed:**
Cyclical pattern where soil moisture decreases during daylight hours and recovers at night.

**Environmental insights:**
- Higher daytime temperatures and light levels increase evaporation and plant water uptake
- Natural daily cycles affect plant water stress

**Watering system performance:**
- Automated system successfully maintains moisture levels
- Pumps activate when moisture drops below 35% threshold
- Saw-tooth pattern indicates system working as designed

---

## Question 8: What does the histogram tell you about the temperature environment? Based on the scatter plot, what is the general relationship between temperature and soil moisture?

**Histogram Analysis:**
- **Bimodal distribution** with peaks around 16°C and 24°C
- Dip around 20°C indicates clear daily temperature cycles
- Cooler temperatures during night/early morning, warmer during daytime
- Typical pattern for indoor environments with natural temperature fluctuations

**Scatter Plot Analysis:**
- **Negative correlation** between temperature and soil moisture
- As temperature increases, soil moisture decreases
- Consistent with higher evaporation rates and increased plant water uptake at higher temperatures
- Outlier points (likely sensor B-1) show unusually high moisture values regardless of temperature, suggesting sensor malfunction (Asked AI)

---

## Final Challenge

### Visualizations
### Faulty Sensor Analysis
**Sensor identification:** 
**Justification:** 

---