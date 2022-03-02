"""Unit test for the floodwarnings module"""

from floodsystem.station import MonitoringStation
from floodsystem.floodwarnings import rank_risk

def test_rank_risk():
    # Create 3 stations to test
    s_id = "test-s1-id"
    m_id = "test-m1-id"
    label = "station 1"
    coord = (-2.0, 4.0)
    trange = (0, 5)
    river = "River X"
    town = "My Town"
    s1 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    s1.latest_level = -2

    s_id = "test-s2-id"
    m_id = "test-m2-id"
    label = "station 2"
    coord = (-2.0, 4.0)
    trange = (0, 5)
    river = "River X"
    town = "My Town"
    s2 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    s2.latest_level = 3

    s_id = "test-s3-id"
    m_id = "test-m3-id"
    label = "station 3"
    coord = (-2.0, 4.0)
    trange = (0, 5)
    river = "River X"
    town = "My Town"
    s3 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    s3.latest_level = 5

    # Verify test
    stations = [s1, s2, s3]
    tol = 0.5

    ranked_risk = rank_risk(stations, tol)

    assert len(ranked_risk) == 2
    assert ranked_risk[0] == ('station 3', 1.0)
    assert ranked_risk[1] == ('station 2', 0.6)


