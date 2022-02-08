from floodsystem.stationdata import build_station_list
import floodsystem.geo 

def test_stations_by_distance():
    stations = build_station_list()
    p = (52.2053, 0.1218)
    distance = floodsystem.geo.stations_by_distance(stations, p) 
    assert distance[0][1] == 0.840237595667494
    assert distance[1][1] == 2.502277543239629

def test_stations_within_radius():
    stations = build_station_list()
    centre = (52.2053, 0.1218)
    r = 20 
    assert floodsystem.geo.stations_within_radius(stations, centre, r)[19][1] == 15.384913680189234

def test_rivers_with_station():
    stations = build_station_list()
    assert floodsystem.geo.len(rivers_with_station(stations)) == 950
    assert floodsystem.geo.rivers_with_station[0] == "Addlestone Bourne"
    assert floodsystem.geo.rivers_with_station[1] == "Aire Washlands"

def test_stations_by_river():
    stations = build_station_list()
    assert floodsystem.geo.stations_by_river["River Aire"][1] == "Apperley Bridge"
    assert floodsystem.geo.stations_by_river["River Aire"][2] == "Armley"
    assert floodsystem.geo.stations_by_river["River Cam"][0] == "Cam"

def test_rivers_by_station_number():
    stations = build_station_list()
    



    


