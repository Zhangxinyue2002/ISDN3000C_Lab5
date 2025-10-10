# ISDN3000C Lab 5: Smart Garden Sensor Data Analysis

## Overview

This project involves analyzing sensor data from a smart garden monitoring system to identify faulty sensors and understand plant health patterns. The lab focuses on data analysis techniques using Python libraries including pandas, numpy, and matplotlib to process time-series sensor data from multiple plant monitoring devices.

## Project Structure

```
ISDN3000C_Lab5/
├── getting_started.py      # Data generation script for plant sensor simulation
├── part1.py               # Basic array operations and statistical analysis
├── part2.py               # Data preprocessing and pandas operations
├── part3.py               # Data visualization with matplotlib
├── final_challenge.ipynb  # Comprehensive sensor fault detection analysis
├── questions.md           # Lab exercise answers and explanations
├── requirements.txt       # Python dependencies
└── readme.md             # This file
```

## Dataset Description

The project uses simulated sensor data from a smart garden monitoring system with the following characteristics:

- **Time Period**: July 1-31, 2023 (hourly readings)
- **Sensors**: 5 plant monitoring devices (A-1, A-2, B-1, B-2, C-1)
- **Locations**: Living Room, Office, Patio
- **Plant Types**: Fiddle Leaf Fig, Monstera, Snake Plant, Pothos, Tomato
- **Measurements**: Temperature (Celsius), Soil Moisture (%), Light Level (Lux)

### Data Features

- `timestamp`: Date and time of measurement
- `sensor_id`: Unique identifier for each sensor
- `plant_type`: Type of plant being monitored
- `location`: Physical location of the sensor
- `temperature_c`: Temperature in Celsius
- `soil_moisture`: Soil moisture percentage
- `light_level`: Light intensity in Lux

## Requirements

Install the required Python packages using:

```bash
pip install -r requirements.txt
```

Required packages:
- pandas
- numpy
- matplotlib
- notebook (for Jupyter notebook)

## Lab Components

### Part 1: Array Basics (part1.py)
- Basic numpy array operations
- Statistical calculations (mean, median, standard deviation)
- Boolean indexing and filtering
- Array slicing techniques

### Part 2: Data Preprocessing (part2.py)
- Data loading and inspection
- Data type conversions (timestamp handling)
- Unit conversions (Celsius to Fahrenheit)
- Missing data handling

### Part 3: Data Visualization (part3.py)
- Bar charts for sensor comparisons
- Time series plotting
- Multiple subplot arrangements
- Data aggregation and grouping

### Final Challenge: Fault Detection (final_challenge.ipynb)
A comprehensive Jupyter notebook implementing multiple analysis techniques:

1. **Statistical Summary Analysis**
   - Mean, median, standard deviation calculations per sensor
   - Variability detection for identifying erratic behavior

2. **Outlier Detection**
   - Interquartile range (IQR) method
   - Identification of impossible readings
   - Percentage-based outlier analysis

3. **Correlation Analysis**
   - Cross-sensor correlation comparison
   - Pattern similarity detection
   - Environmental response analysis

4. **Visualization Dashboard**
   - Multi-panel dashboard with 4 key visualizations
   - Bar charts, box plots, time series, and variability plots
   - Automated fault identification

## Key Findings

The analysis successfully identifies **Sensor B-1** as the faulty device based on:
- Highest variability in readings (standard deviation > 20)
- Significant outlier patterns with impossible values (>90% moisture)
- Poor correlation with environmental factors
- Erratic behavior in time series visualization

## Data Generation Details

The sensor data is artificially generated with realistic patterns:
- Temperature follows diurnal cycles with peak afternoon values
- Light levels correlate with time of day
- Soil moisture includes natural variation
- **Sensor B-1 intentionally includes faults** (10% chance of extreme values)

## Learning Objectives

This lab demonstrates:
- Real-world data analysis workflows
- Statistical methods for quality assurance
- Time series data handling
- Visualization techniques for data exploration
- Fault detection in IoT sensor networks
- Python data science stack proficiency

## Usage

1. Run `getting_started.py` to generate the sensor data
2. Complete exercises in `part1.py`, `part2.py`, and `part3.py`
3. Work through the comprehensive analysis in `final_challenge.ipynb`
4. Review answers and explanations in `questions.md`

## Technical Notes

- All scripts use `np.random.seed(42)` for reproducible results
- Data includes intentional missing values and sensor faults for realistic analysis
- Time series data spans 721 hours (July 1-31, 2023)
- Analysis techniques are applicable to real IoT sensor monitoring systems