import numpy as np
import matplotlib


"""
def polyfit(dates, levels, p):
    conv_dates = matplotlib.dates.date2num(dates)
    d0 = 1
    shifted_dates = conv_dates - conv_dates[-d0]
    coefficients = np.polyfit(shifted_dates, levels, p)
    polynomial = np.poly1d(coefficients)
    return polynomial, d0
"""
def polyfit(dates, levels, p):
    x = matplotlib.dates.date2num(dates)
    y = levels
    p_coefficient = np.polyfit(x-x[0], y, p)
    poly = np.poly1d(p_coefficient)
    return poly, x[0]