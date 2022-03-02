from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.floodwarnings import rank_risk

def run():
    # Build list of stations and type for which tolerance value we are testing
    stations = build_station_list()
    tolerance = 0.5

    #Update our values
    update_water_levels(stations)
    ranked_risk = rank_risk(stations, tolerance)
    print("These stations have a low risk of flooding:", ranked_risk[0], "\n")
    print("These stations have a moderate risk of flooding:", ranked_risk[1], "\n")
    print("These stations have a high risk of flooding:", ranked_risk[2], "\n")
    print("These stations have a severe risk of flooding:", ranked_risk[3])

    
if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()