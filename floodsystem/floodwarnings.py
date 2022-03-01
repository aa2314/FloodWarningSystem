from floodsystem.flood import stations_level_over_threshold
from floodsystem.datafetcher import fetch_measure_levels
import datetime
from floodsystem.utils import sorted_by_key

def rank_risk(stations, tol):
    """This function ranks the towns where the risk of flooding is greatest.
    First of all, we only consider towns where tolerance is high enough, typically tol = 0.5.
    Then we list the stations according to the greatest difference in levels as they are the most dangerous.
    We then return the names of towns in the 4 distinct categories"""

    level_change = []
    
    # Only consider stations with a relative water level above the decided tolerance
    # Then sort stations by largest level difference between minimum and maxiumum values
    for station in stations:
        if station.relative_water_level() != None:
            if station.relative_water_level() > 1.0:
                dates, levels = fetch_measure_levels(station.measure_id, dt = datetime.timedelta(days = 2))
                if len(levels) > 0:
                    delta_levels = max(levels) - min(levels)
                    level_change.append((station.name, delta_levels))
        
    delta_levels_sorted = sorted_by_key(level_change, 1, reverse = True)
    
    # Seperate the stations in 4 approximately equal categories
    low_risk = delta_levels_sorted[:int(len(delta_levels_sorted)*0.25):]
    moderate_risk = delta_levels_sorted[int(len(delta_levels_sorted)*0.25):int(len(delta_levels_sorted)*0.5)]
    high_risk = delta_levels_sorted[int(len(delta_levels_sorted)*0.5):int(len(delta_levels_sorted)*0.75)]
    severe_risk = delta_levels_sorted[int(len(delta_levels_sorted)*0.75):]

    # From these categories, only take the names of the stations
    low_stations = [data[0] for data in low_risk]
    moderate_stations = [data[0] for data in moderate_risk]
    high_stations = [data[0] for data in high_risk]
    severe_stations = [data[0] for data in severe_risk]

    return print("These stations have a low risk of flooding:", low_stations, "\n",
    "These stations have a moderate risk of flooding:", moderate_stations, "\n", 
    "These stations have a high risk of flooding:", high_stations, "\n", 
    "These stations have a severe risk of flooding:", severe_stations)
