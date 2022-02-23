from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level

def run():
    # Build list of stations and type for which tolerance value we are testing
    stations = build_station_list()

    #Update our values
    update_water_levels(stations)
    print(stations_highest_rel_level(stations, 10))
    
    

if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()