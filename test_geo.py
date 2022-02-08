from floodsystem.stationdata import build_station_list
import floodsystem.geo 

def test_stations_by_distance():
    stations = build_station_list()
    p = (52.2053, 0.1218)
    distances = floodsystem.geo.stations_by_distance(stations, p) 
    for i in range(len(stations)-1):
        assert distances[i][1] <= distances[i+1][1] 

    assert distances[0][1] == 0.840237595667494
    assert distances[1][1] == 2.502277543239629
    

def test_stations_within_radius():
    stations = build_station_list()
    centre = (52.2053, 0.1218)
    r = 20 
    list_radius = floodsystem.geo.stations_within_radius(stations, centre, r)
    for i in range(len(list_radius)):
        assert floodsystem.geo.stations_within_radius(stations, centre, r)[i][1] <= 20
    assert floodsystem.geo.stations_within_radius(stations, centre, r)[19][1] == 15.377426364326626

def test_rivers_with_station():
    stations = build_station_list()
    liste = floodsystem.geo.rivers_with_station(stations)
    assert len(liste) == 950
    assert liste[0] == "Addlestone Bourne"
    assert liste[1] == "Aire Washlands"

def test_stations_by_river():
    stations = build_station_list()
    dictionary = floodsystem.geo.stations_by_river(stations)
    for key in dictionary.keys():
        for station in dictionary[key]:
            assert key == station.river
    assert type(dictionary) == type({})
    assert dictionary["River Aire"][1] == "Apperley Bridge"
    assert dictionary["River Aire"][2] == "Armley"
    assert dictionary["River Cam"][0] == "Cam"



def test_rivers_by_station_number():
    stations = build_station_list()
    assert floodsystem.geo.rivers_by_station_number(stations, N = 5)[1][1] == 31
    assert floodsystem.geo.rivers_by_station_number(stations, N = 5)[1][0] == "River Avon"
    assert floodsystem.geo.rivers_by_station_number(stations, N = 5)[3][1] == 25
    rivers_by_station_num = floodsystem.geo.rivers_by_station_number(stations, N = 10)
    for station in range(len(rivers_by_station_num)-1):
           assert rivers_by_station_num[station][1] >= rivers_by_station_num[station+1][1]
           assert type(rivers_by_station_num[station][0]) == type("ABC")




    


