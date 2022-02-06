from scipy.fftpack import ss_diff
from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river

def first_run():
    stations = build_station_list()
    print(rivers_with_station(stations)[:10])
    print("There are {} stations in total.". format(len(rivers_with_station(stations))))

def second_run():
    stations = build_station_list()
    print(sorted(stations_by_river(stations)["River Aire"]))





if __name__ == "__main__":
    print("*** Task 1A: CUED Part IA Flood Warning System ***")
    print("***TEST 1***")
    first_run()
    print("***TEST 2***")
    second_run()
     


