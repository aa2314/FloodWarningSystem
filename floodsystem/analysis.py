import numpy as np
import matplotlib


def polyfit(dates, levels, p):
    conv_dates = matplotlib.dates.date2num(dates)
    d0 = 1
    shifted_dates = conv_dates[d0:]
    coefficients = np.polyfit(shifted_dates, levels, p)
    polynomial = np.poly1d(coefficients)
    tpl = (polynomial, d0)
    return tpl 


    


