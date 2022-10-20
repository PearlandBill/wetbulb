''' Wetbulb entity class'''
from __future__ import annotations

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

    def __init__(self, hass, wb_config):
        
        #https://developers.home-assistant.io/docs/device_registry_index/#defining-devices
#        _attr_unique_id = wb_config.unique_id

#        _attr_has_entity_name = True

        #https://developers.home-assistant.io/docs/core/entity/sensor
#        device_class = DEVICE_CLASS_TEMPERATURE
#        native_value = int

        #error with below
        #self.name = wb_config.name  # did not change unnamed entity
        #self.name error = /home/bill/github/home-assistant/core/config/.storage/input_datetime'

 #       entity_description = WebBulbEntityDescription(
 #           device_class = SensorDeviceClass.TEMPERATURE,
 #           last_reset = datetime.now,
 #           native_unit_of_measurement = TEMP_FAHRENHEIT,
 #           state_class = SensorStateClass.MEASUREMENT,
 #           unit_of_measure = None
 #       )

        

        # Make entity id
        entityId = "sensor." + wb_config.name
        entityId = entityId.replace(" ", "_")
        entityId = entityId.lower()

 #       entity_id = entityId

        self.wb_config = wb_config
        self.wb_config.wetbulb_entity = entityId
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

        #get the temperature
        temp_entity = self.hass.states.get(self.wb_config.temp_sensor)
        rh_entity = self.hass.states.get(self.wb_config.rh_sensor)

        # Validate values
        try:
            temp = float(temp_entity.state)
            rh = int(rh_entity.state)

            # find wet bulb
            wb = calculator.calcwb(temp, rh, self.wb_config.number_of_digits, 'F')

            # set state
            #self.hass.states.set(self.wetbulb_entity, wb)
            self._attr_native_value = wb
            #self.schedule_update_ha_state(True)
            _LOGGER.info("wb state for " + self.wb_config.wetbulb_entity + " has been set")

            return True
        except Exception as e:
            self._state = "Error"
            self.schedule_update_ha_state()
            _LOGGER.error("Error updating the web bulb temperature")
            _LOGGER.error(e)
            return False

        
    