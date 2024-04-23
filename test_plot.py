from floodsystem.station import MonitoringStation
from floodsystem.plot import *
from floodsystem.stationdata import build_station_list
from floodsystem.datafetcher import fetch_measure_levels
import matplotlib.pyplot as plt
import random
import datetime



def test_plot_water_level_with_fit():
    """Function that choses three random stations from the station list and displays them. The graphs then be compared to
    actal data provided on the government website. Also checks if the least squares plot has the right shape."""
    stations = build_station_list()
    p = 5
    for i in range(3):
        rand_number = random.randint(0,len(stations))
        dates, levels = fetch_measure_levels(stations[rand_number].measure_id,dt = datetime.timedelta(days = 10))
        plot_water_level_with_fit(stations[rand_number],dates,levels,p)
    
    polynomial, d0 = polyfit(dates, levels, p)
    assert type(polynomial) == type(np.poly1d([1,2,3]))
    assert len(np.roots(np.polyder(polynomial, 1))) == p-1
