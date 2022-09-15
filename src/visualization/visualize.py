import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import sys
import os
import datetime

sys.path.append("..")
import utility.plot_settings

class PlotData():
    
    def __init__(self) -> None:
        pass
    
    def _export_figure(self, filename):

        date = datetime.date.today().strftime("%d-%m-%Y")
        path = f"../../reports/figures/{date}/"

        if os.path.exists(path):
            plt.savefig(path + filename + ".png", bbox_inches="tight")

        if not os.path.exists(path):
            os.makedirs(path)
            plt.savefig(path + filename + ".png", bbox_inches="tight")

        print(f"Successfully export {filename}")
    
    def motor_power(self, df):

        # Create canvas
        fig, ax1 = plt.subplots()

        # Make plots
        ax1.plot(df.index, df["Motor Active Power"], label="Motor Active Power")
        ax1.plot(df.index, df["Motor Apparent Power"], label="Motor Apparent Power")
        ax1.plot(df.index, df["Motor Reactive Power"], label="Motor Reactive Power")
        ax1.plot(df.index, df["Motor Shaft Power"], label="Motor Shaft Power")

        # Adjust date ticks
        ax1.xaxis.set_major_locator(mdates.DayLocator(interval=1))
        ax1.xaxis.set_major_formatter(mdates.DateFormatter("%d-%m-%Y"))

        # Adjust y-ticks and limits
        y1_min = 12
        y1_max = 17

        ax1.set_ylim([y1_min, y1_max])
        ax1.set_yticks(np.arange(y1_min, y1_max + 1, 1))

        # Set labels
        ax1.set_title("Motor Power")
        ax1.set_xlabel("Timestamp", color="black")
        ax1.set_ylabel("Power (W)", color="black")

        # Set legend
        fig.legend(loc="upper right", bbox_to_anchor=(1, 1), bbox_transform=ax1.transAxes)

        # Styling
        ax1.grid(True)
        ax1.tick_params(left=False, bottom=False, color="black")

        # Export figure
        self._export_figure(filename="Motor Power (4x)")

        # Show plot in interactive Python
        plt.show()
    
    def speed_vs_temp(self, df):

        # Create canvas
        fig, ax1 = plt.subplots()
        ax2 = ax1.twinx()

        # Make plots
        ax1.plot(df.index, df["Motor Active Power"], label="Motor Active Power")
        ax2.plot(
            df.index,
            df["Pump Temp (C)"],
            label="Pump Temperature",
            color="black",
            linestyle="--",
            alpha=0.25,
        )

        # Adjust date ticks
        ax1.xaxis.set_major_locator(mdates.DayLocator(interval=1))
        ax1.xaxis.set_major_formatter(mdates.DateFormatter("%d-%m-%Y"))

        # Adjust y-ticks and limits
        y1_min = 12.5
        y1_max = 14
        y2_min = 0
        y2_max = 60

        ax1.set_ylim([y1_min, y1_max])
        ax2.set_ylim([y2_min, y2_max])

        ax1.set_yticks(np.arange(y1_min, y1_max + 1, 0.5))

        # Set labels
        ax1.set_title("Motor Speed vs. Temperature")
        ax1.set_xlabel("Timestamp", color="black")
        ax1.set_ylabel("Power (W)", color="black")
        ax2.set_ylabel("Temperature (C)", color="black")

        # Set legend
        fig.legend(loc="upper right", bbox_to_anchor=(1, 1), bbox_transform=ax1.transAxes)

        # Styling
        ax1.grid(True)
        ax2.grid(False)
        ax1.tick_params(left=False, bottom=False)
        ax2.tick_params(right=False, bottom=False)

        # Export figure
        self._export_figure(filename="Motor Speed vs. Temperature")

        # Show plot in interactive Python
        plt.show()

    
    
    