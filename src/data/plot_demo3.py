import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

sys.path.append("..")
import utility.plot_settings


# --------------------------------------------------------------
# Import data
# --------------------------------------------------------------

data = pd.read_csv(
    "../../data/raw/pump_sensor_data.csv",
    parse_dates=[0],
    index_col=[0],
)

data["sensor_00"].plot()

# Plot columns in a loop
for col in data.columns[:5]:
    data[col].plot()
    plt.show()
