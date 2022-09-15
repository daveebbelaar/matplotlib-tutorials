import pandas as pd

# --------------------------------------------------------------
# 1. Define objective
# --------------------------------------------------------------

""" 
The objective of this script is to create 2 figures for a report 
to evaluate pump performance.

Figures
- Motor power (4x)
- Motor speed vs. pump temperature in celsius

"""

# --------------------------------------------------------------
# 2. Read raw data
# --------------------------------------------------------------

data = pd.read_csv(
    "../../data/raw/pump_sensor_data.csv", parse_dates=[0], index_col=[0]
)


# --------------------------------------------------------------
# 3. Process data
# --------------------------------------------------------------

# Select first 10 columns
subset = data.iloc[:, :10]

# Merge sensor 49
subset = pd.merge(subset, data["sensor_49"], left_index=True, right_index=True)


# Rename columns
cols = [
    "Motor Casing Vibration",
    "Motor Frequency A",
    "Motor Frequency B",
    "Motor Frequency C",
    "Motor Speed",
    "Motor Current",
    "Motor Active Power",
    "Motor Apparent Power",
    "Motor Reactive Power",
    "Motor Shaft Power",
    "Pump Temp",
]
subset.columns = cols


# --------------------------------------------------------------
# Export
# --------------------------------------------------------------

subset.to_pickle("../../data/interim/pump_sensor_data_subset.pkl")
