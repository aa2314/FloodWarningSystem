# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation
import floodsystem.station
from floodsystem.stationdata import build_station_list


def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town

def test_inconsistent_typical_range_stations():
    stations = build_station_list()
    liste = floodsystem.station.inconsistent_typical_range_stations(stations)
    assert len(liste) == 28


def test_relative_water_level():
    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    
    # Set a value for latest level
    s.latest_level = -2.3
    # Check if relative water level is what is expected
    assert s.relative_water_level() == 0 ## latest value is the minimum hence relative water level should be 0

    # Likewise, we can check if this will work for the maximum value of the typical range
    s.latest_level = 3.4445
    assert s.relative_water_level() == 1

