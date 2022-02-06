# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""


from .utils import sorted_by_key
from haversine import haversine


def stations_by_distance(stations, p):
    """Given a list of station objects and a coordinate p, 
    returns a list of (station, distance) tuples, 
    where distance (float) is the distance of the station (MonitoringStation) from the coordinate p."""
    list_stations = []
    for station in stations:
        list_stations.append((station.name, haversine(station.coord, p)))
    list_stations = sorted_by_key(list_stations, 1)
    return list_stations

def stations_within_radius(stations, centre, r):
    """ returns a list of all stations within radius r of a geographic coordinate x """
    stations_within_R = []
    for station in stations:
        if haversine(station.coord, centre) <= r :
            stations_within_R.append((station.name, haversine(station.coord, centre))) 
    return sorted(stations_within_R)

def rivers_with_station(stations):
    """given a list of station objects, returns a container (list/tuple/set) with the names
       of the rivers with a monitoring station.
    """
    rivers_with_st = set()
    for station in stations:
        rivers_with_st.add(station.river)
    return sorted(rivers_with_st)

def stations_by_river(stations):
    """returns a dictionary that maps river names to a list of station objects on a given river.
    """
    st_by_river = {}
    for river in rivers_with_station(stations):
        liste = []
        for station in stations:
            if station.river == river:
                liste.append(station.name)
        st_by_river[river] = liste
    return st_by_river 

def rivers_by_station_number(stations, N):
    """Determines the N rivers with the greatest number of monitoring stations. 
    Returns a list of (river name, number of stations) tuples, sorted by the number of stations. 
    If more rivers with the same number of stations as the N th entry, include these rivers in the list. """

    # Find length of number of stations on given river
    river_num = []
    rivers = stations_by_river(stations)
    for river_name in rivers:
        river_num.append((river_name, len(rivers[river_name])))

    # Sort tuples by number of stations on river
    river_num_sort = sorted_by_key(river_num, 1, reverse=True)
    river_num_final = []

    # Collect first N values
    for i in range(N):
        river_num_final.append(river_num_sort[i]) 

    # If any other rivers also have the same number of stations as the last one of the list, also add them to the list
    for river in river_num_sort:
        if river[1] == river_num_final[N][1]:
                river_num_final.append(river)
        else:
            break

    return river_num_final 