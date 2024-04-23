"""Unit test for the floodwarnings module"""

from distutils.command.build import build
from floodsystem.station import MonitoringStation
from floodsystem.floodwarnings import rank_risk
from floodsystem.stationdata import build_station_list, update_water_levels

def test_rank_risk():
    '''
    # Create 3 stations to test
    coord = (-2.0, 4.0)
    trange = (0, 5)
    river = "River X"
    town = "My Town"

    s1 = MonitoringStation("test-s1-id", "test-m1-id", "station 1", coord, trange, river, town)
    s1.latest_level = 0

    s2 = MonitoringStation("test-s2-id", "test-m2-id", "station 2", coord, trange, river, town)
    s2.latest_level = 3

    s3 = MonitoringStation("test-s3-id", "test-m3-id", "station 3", coord, trange, river, town)
    s3.latest_level = 5

    s4 = MonitoringStation("test-s4-id", "test-m4-id", "station 4", coord, trange, river, town)
    s4.latest_level = 3.5

    s5 = MonitoringStation("test-s5-id", "test-m5-id", "station 5", coord, trange, river, town)
    s5.latest_level = 4
    '''

    # Verify test
    stations = build_station_list()
    tol = 0.5
    update_water_levels(stations)

    ranked_risk = rank_risk(stations, tol)

    assert ranked_risk[3][-1] == "Fordham"

