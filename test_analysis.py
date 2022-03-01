import numpy as np
import matplotlib
from floodsystem.stationdata import *
from floodsystem.analysis import *
from datetime import datetime

def test_polyfit():
    dates = [1,2,3,4,5]
    levels = [1,4,9,16,25]
    p = 4
    polynomial, d0 = polyfit(dates, levels, p)
    assert type(polynomial) == type(np.poly1d([1,2,3]))
    assert len(np.roots(np.polyder(polynomial, 1))) == 3

