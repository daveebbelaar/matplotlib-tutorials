import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt


# --------------------------------------------------------------
# Setting rcParams
# --------------------------------------------------------------

from cycler import cycler

colors = cycler(color=plt.get_cmap("tab10").colors)  # ["b", "r", "g"]

mpl.style.use("ggplot")
mpl.rcParams["figure.figsize"] = (20, 5)
mpl.rcParams["axes.facecolor"] = "white"
mpl.rcParams["axes.grid"] = True
mpl.rcParams["grid.color"] = "lightgray"
mpl.rcParams["axes.prop_cycle"] = colors
mpl.rcParams["axes.linewidth"] = 1
mpl.rcParams["xtick.color"] = "black"
mpl.rcParams["ytick.color"] = "black"
mpl.rcParams["font.size"] = 12
mpl.rcParams["figure.titlesize"] = 25
mpl.rcParams["figure.dpi"] = 100


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
    data[col].plot()
    plt.show()
