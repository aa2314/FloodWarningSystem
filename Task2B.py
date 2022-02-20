from floodsystem.stationdata import build_station_list, update_water_levels, relative_water_level 
from floodsystem.flood import stations_level_over_threshold

def run():
    # Build list of stations and type for which tolerance value we are testing
    stations = build_station_list()
    tol = 0.8

    print(stations_level_over_threshold(stations, tol))

if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()
