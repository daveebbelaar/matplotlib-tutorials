import pandas as pd


data = pd.read_pickle("../../data/interim/pump_sensor_data_subset.pkl")

# --------------------------------------------------------------
# 4. Apply business logic
# --------------------------------------------------------------


def fahrenheit_to_celsius(series):
    """Function to convert fahrenheit to celsius

    Args:
        series pd.Series: Pandas Series or DataFrame to convert

    Returns:
        pd.Series: Converted Series or DataFrame
    """
    return (series - 32) / 1.8


data["Pump Temp (C)"] = fahrenheit_to_celsius(data["Pump Temp"])

# --------------------------------------------------------------
# Export data
# --------------------------------------------------------------

data.to_pickle("../../data/processed/subset_sensor_data_processed.pkl")
