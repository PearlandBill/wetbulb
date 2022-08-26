'''Calculate the wet bulb temp from temp and relative humidity'''

# The most important formula to compute the wet bulb temperature is 
# Tw = T * arctan[0.151977 * (rh% + 8.313659)^(1/2)] +     atan1
# arctan(T + rh%) -     atan2
# arctan(rh% - 1.676331) +     atan3
# 0.00391838 *(rh%)^(3/2) *     factor1
# arctan(0.023101 * rh%) -     atan4
# 4.686035    
# Here rh is the relative humidity and T is the temperature.

# https://physicscalc.com/physics/wet-bulb-calculator/#:~:text=The%20most%20important%20formula%20to,0.023101%20*%20rh%25)%20%2D%204.686035.

import math
from wetbulb_config_data import wb_config

def calcwb(temp: float, rh: int, num_digits: int, unit_of_measure: str) -> float:
    #Convert temp to Celsius

    # assume that the temp is in celsius
    tempC = temp

    # check for celsius
    if unit_of_measure == 'F':
        tempC = (temp - 32) * 5/9

    #Calc wet bulb
    atan1 = math.atan(0.151977 * math.pow((rh + 8.313659), 1/2))
    atan2 = math.atan(temp + rh)
    atan3 = math.atan(rh - 1.676331)
    atan4 = math.atan(0.023101 * rh)
    factor1 = 0.00391838 * math.pow(rh, 3/2)

    wb = tempC * atan1 + atan2 - atan3 + factor1 * atan4 - 4.686035

    #convert wb to farenheit?
    if unit_of_measure == 'F':
        wb = (wb * 9/5) + 32

    # round wb
    wb = round(wb, num_digits)

    return wb

t = 89
r = 59
num_decimals = 0
unit_of_measure = 'F'

wb = calcwb(t, r, num_decimals, unit_of_measure)

config = wb_config('F', 'outdoor temp entity name', 'outdoor rh entity name')
config.unit_of_measure = unit_of_measure
config.outdoor_temp_entity = t
config.outdoor_rh_entity = r
config.indoor_temp_entity = 'in xyz'
config.indoor_rh_entity = 'in abc'

print(f"Web bulb = {config}")
print(wb)
print(f'Config is valid = {config.is_valid()}')


