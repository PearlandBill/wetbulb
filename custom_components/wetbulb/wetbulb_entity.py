''' Wetbulb entity class'''
from __future__ import annotations
from pyparsing import replace_html_entity
from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorStateClass,
)
from homeassistant.const import TEMP_FAHRENHEIT
from . import calculator
import logging

class WetBulbEntity(SensorEntity):
    """Representation of a Wet Bulb Sensor."""

    _attr_name = "Wet Bulb Temperature"
    _attr_native_unit_of_measurement = TEMP_FAHRENHEIT
    _attr_device_class = SensorDeviceClass.TEMPERATURE
    _attr_state_class = SensorStateClass.MEASUREMENT
    
    def __init__(self, hass, temp_entity, rh_entity, num_digits):

        self.temp_entity = temp_entity
        self.rh_entity = rh_entity
        self.num_digits = num_digits
        self.hass = hass

    @property
    def device_info(self):
        return {
            "name": self.name,
        }

    @property
    def should_poll(self):
        return True

    def update(self):
        # Log that update is happening
        _LOGGER = logging.getLogger(__name__)

        #get the temperature and rh entities
        temp_entity = self.hass.states.get(self.temp_entity)
        rh_entity = self.hass.states.get(self.rh_entity)

        uom = temp_entity.attributes['unit_of_measurement']

        # Validate values
        try:
            #get temp and rh values
            temp = float(temp_entity.state)
            rh = int(rh_entity.state)

            # find wet bulb
            wb = calculator.calcwb(temp, rh, uom)

            #round the wet bulb temp
            wb = round(wb, self.num_digits)

            #if the num_digits is zero, round will not work properly, convert to int
            if self.num_digits == 0:
                wb = int(wb)

            # set state
            self._attr_native_value = wb
            _LOGGER.info(f"Wet bulb state for {self._attr_name} has been set")

            return True
        except Exception as e:
            self._state = "Error"
            self.schedule_update_ha_state()
            _LOGGER.error("Error updating the web bulb temperature")
            _LOGGER.error(e)
            return False

        
    