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