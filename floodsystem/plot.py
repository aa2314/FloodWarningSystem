import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from floodsystem.analysis import polyfit

def plot_water_levels(station, dates, levels): 
    """function that displays a plot of the water level data against time for a station"""

    plt.plot(dates, levels)
    plt.xlabel("Date")
    plt.ylabel("Water Level")
    plt.title("Station: {}".format(station.name))
    plt.xticks(rotation=30)
    plt.tight_layout()
    return plt.show()

def plot_water_level_with_fit(station, dates, levels, p):
    plt.plot(dates, levels)
    plt.plot(polyfit(dates, levels, p)[0], levels)
    plt.xlabel("Date")
    plt.ylabel("Water Level")
    plt.title("Station: {}".format(station.name))
    plt.xticks(rotation=30)
    plt.tight_layout()
