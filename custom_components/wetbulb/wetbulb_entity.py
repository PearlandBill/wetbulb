''' Wetbulb entity class'''
from __future__ import annotations

from pyparsing import replace_html_entity

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorStateClass,
)
from homeassistant.const import DEVICE_CLASS_AQI, DEVICE_CLASS_TEMPERATURE, TEMP_CELSIUS, TEMP_FAHRENHEIT
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType
#from homeassistant.components.sensor import SensorEntity
from . import calculator
from . import wetbulb_config
import logging
from datetime import date, datetime, timedelta, timezone

DOMAIN = 'wetbulb'

#class WebBulbEntityDescription(SensorEntityDescription):
#    '''A class for defining the web bulb sensor entity description'''
#
#    device_class: SensorDeviceClass | str | None = None
#    last_reset: datetime | None = None
#    native_unit_of_measurement: str | None = None
#    state_class: SensorStateClass | str | None = None
#    unit_of_measurement: None = None  # Type override, use native_unit_of_measurement


class WetBulbEntity(SensorEntity):
    """Representation of a Sensor."""

    _attr_name = "Wet Bulb Temperature"
    _attr_native_unit_of_measurement = TEMP_FAHRENHEIT
    _attr_device_class = SensorDeviceClass.TEMPERATURE
    _attr_state_class = SensorStateClass.MEASUREMENT
    

    def __init__(self, hass, temp_entity, rh_entity, num_digits):

        self.temp_entity = temp_entity
        self.rh_entity = rh_entity
        self.num_digits = num_digits

        self.hass = hass

    #https://developers.home-assistant.io/docs/device_registry_index/#defining-devices
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

        # Validate values
        try:
            #get temp and rh values
            temp = float(temp_entity.state)
            rh = int(rh_entity.state)

            # find wet bulb
            wb = calculator.calcwb(temp, rh, self.num_digits, 'F')

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

        
    