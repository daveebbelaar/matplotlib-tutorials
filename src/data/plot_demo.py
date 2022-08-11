import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

sys.path.append("..")

from utility import plot_settings

data = pd.read_excel(
    "../../data/raw/pump_sensor_data/20180401_pump_sensor_data.xlsx",
    parse_dates=[0],
    index_col=[0],
)
