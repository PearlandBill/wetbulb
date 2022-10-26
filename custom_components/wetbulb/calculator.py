import math
from homeassistant.const import TEMP_FAHRENHEIT

def calcwb(temp: float, rh: int, unit_of_measure: str) -> float:
    #Convert temp to Celsius

    # assume that the temp is in celsius
    tempC = temp

    # check for celsius
    if unit_of_measure == TEMP_FAHRENHEIT:
        tempC = (temp - 32) * 5/9

    #Calc wet bulb
    atan1 = math.atan(0.151977 * math.pow((rh + 8.313659), 1/2))
    atan2 = math.atan(temp + rh)
    atan3 = math.atan(rh - 1.676331)
    atan4 = math.atan(0.023101 * rh)
    factor1 = 0.00391838 * math.pow(rh, 3/2)

    wb = tempC * atan1 + atan2 - atan3 + factor1 * atan4 - 4.686035

    #convert wb to farenheit?
    if unit_of_measure == TEMP_FAHRENHEIT:
        wb = (wb * 9/5) + 32

    return wb
