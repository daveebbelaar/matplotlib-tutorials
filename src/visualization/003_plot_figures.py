import pandas as pd
from visualize import PlotData

# --------------------------------------------------------------
# Load data
# --------------------------------------------------------------

data = pd.read_pickle("../../data/processed/subset_sensor_data_processed.pkl")

# --------------------------------------------------------------
# Create plots
# --------------------------------------------------------------

plot = PlotData()
plot.motor_power(df=data)
plot.speed_vs_temp(df=data)
