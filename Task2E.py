from lib2to3.pgen2.tokenize import StopTokenizing
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_levels
import datetime
import matplotlib as plt
from floodsystem.utils import sorted_by_key


"""def run():
    # Build list of stations and type for which tolerance value we are testing
    stations = build_station_list()
    tol = 0.8

    #Update our values
    update_water_levels(stations)

    print(stations_level_over_threshold(stations, tol)
"""
def run():
    stations = build_station_list()
    update_water_levels(stations)
    stations_by_water_level = []
    for station in stations:
        if station.latest_level == None:
            pass
        elif station.name == "Letcombe Bassett": #Not updated since 2/2/22, write to check if station is updated for past 10 days
            pass
        else:
            stations_by_water_level.append((station.name, station.latest_level))
    sorted_list = sorted_by_key(stations_by_water_level, 1, True)[:5]
    name_list = []
    for i in range(5):
        name_list.append(sorted_list[i][0])
    print(sorted_list)

    for station in stations:
        for p in range (5):
            if station.name == name_list[p]:
                print(station.name)
                dates, levels = fetch_measure_levels(station.measure_id,dt = datetime.timedelta(days = 10))
                plot_water_levels(station, dates, levels)

  

if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()
