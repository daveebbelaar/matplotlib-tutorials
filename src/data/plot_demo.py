import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

sys.path.append("..")
from utility import plot_settings

# --------------------------------------------------------------
# Import data
# --------------------------------------------------------------

data = pd.read_csv(
    "../../data/raw/pump_sensor_data.csv",
    parse_dates=[0],
    index_col=[0],
)
