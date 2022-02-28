import matplotlib
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from floodsystem.analysis import polyfit
import numpy as np

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
    plt.plot(dates, levels, label = "Actual Data")
    f_val = matplotlib.dates.date2num(dates)
    polynomial, d0 = polyfit(dates, levels, p)
    plt.plot(dates, polynomial(f_val - f_val[-d0]))    
    plt.plot(dates, [station.typical_range[0]]*len(f_val), label = "Typical Low")
    plt.plot(dates, [station.typical_range[1]]*len(f_val), label = "Typical High")
    plt.xlabel("Date")
    plt.ylabel("Water Level")
    plt.title("Station: {}".format(station.name))
    plt.xticks(rotation=30)
    plt.tight_layout()
    return plt.show()

