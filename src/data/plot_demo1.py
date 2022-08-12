import pandas as pd
import matplotlib.pyplot as plt


# --------------------------------------------------------------
# Import data
# --------------------------------------------------------------

data = pd.read_csv(
    "../../data/raw/pump_sensor_data.csv",
    parse_dates=[0],
    index_col=[0],
)

# --------------------------------------------------------------
# Plotting data
# --------------------------------------------------------------

# Plot single column
data["sensor_00"].plot()

# Plot columns in a loop
for col in data.columns[:5]:
    data[col].plot(figsize=(20, 5))
    plt.show()
