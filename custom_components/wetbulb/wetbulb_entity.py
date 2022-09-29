''' Wetbulb entity class'''
from homeassistant.const import EVENT_HOMEASSISTANT_START, EVENT_HOMEASSISTANT_STOP
import homeassistant.helpers.config_validation as cv
import voluptuous as vol
from homeassistant.components.sensor import SensorEntity
from . import calculator
import logging

DOMAIN = 'wetbulb'

class WetBulbEntity(SensorEntity):
    def __init__(self, hass, name, temp_entity, rh_entity, wetbulb_entity):
        self.hass = hass
        self._name = name
        self.temp_entity = temp_entity
        self.rh_entity = rh_entity
        self.wetbulb_entity = wetbulb_entity

    @property
    def should_poll(self):
        return True

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name

    @property
    def friendly_name(self):
        return self.friendly_name

    @property
    def temp_entity_name(self):
        return self.temp_entity

    @property
    def rh_entity_name(self):
        return self.rh_entity

    @property
    def wb_entity_name(self):
        return self.wetbulb_entity

    def update(self):
        # Log that update is happening
        _LOGGER = logging.getLogger(__name__)
        _LOGGER.error("wetbulb_entity update has been called.")

        #get the temperature
        temp_entity = self.hass.states.get(self.temp_entity)
        rh_entity = self.hass.states.get(self.rh_entity)
        #_LOGGER.error("temp_entity = " + self.temp_entity + ".")
        _LOGGER.error(repr(temp_entity))

        temp_val = temp_entity.state
        _LOGGER.error("temp_val  " + temp_val)

        rh_val = rh_entity.state
        _LOGGER.error("rh_val = " + rh_val)

        temp = 0
        rh = 0

        # Validate values
        try:
            temp = float(temp_val)
            rh = int(rh_val)
        except:
            return False

        # find wet bulb
        _LOGGER.error("Calculating wb.")
        _LOGGER.error("temp = " + str(temp))
        _LOGGER.error("rh = " + str(rh))
        wb = calculator.calcwb(temp, rh, 2, 'F')
        _LOGGER.error("wb = " + str(wb))

        # set state
        self.hass.states.set(self.wetbulb_entity, str(wb))
        _LOGGER.error(repr(self.wetbulb_entity))
        _LOGGER.error("wb state has been set")

        return True

    