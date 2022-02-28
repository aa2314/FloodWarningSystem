from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.floodwarnings import rank_risk

def run():
    # Build list of stations and type for which tolerance value we are testing
    stations = build_station_list()
    tolerance = 0.5

    #Update our values
    update_water_levels(stations)
    print(rank_risk(stations, tolerance))
    
if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()