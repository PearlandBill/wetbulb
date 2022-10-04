''' Wetbulb entity class'''
from homeassistant.const import EVENT_HOMEASSISTANT_START, EVENT_HOMEASSISTANT_STOP
import homeassistant.helpers.config_validation as cv
import voluptuous as vol
from homeassistant.components.sensor import SensorEntity
from . import calculator
import logging

DOMAIN = 'wetbulb'

class WetBulbEntity(SensorEntity):
    def __init__(self, hass, name, temp_entity, rh_entity, wetbulb_entity, config):
        self.hass = hass
        self._name = name
        self.temp_entity = temp_entity
        self.rh_entity = rh_entity
        self.wetbulb_entity = wetbulb_entity
        self.config = config

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

        #get the temperature
        temp_entity = self.hass.states.get(self.temp_entity)
        rh_entity = self.hass.states.get(self.rh_entity)

        # Validate values
        try:
            temp = float(temp_entity.state)
            rh = int(rh_entity.state)

            # find wet bulb
            wb = calculator.calcwb(temp, rh, self.config.number_of_digits, self.config.unit_of_measure)

            # set state
            self.hass.states.set(self.wetbulb_entity, str(wb))
            _LOGGER.info("wb state for " + self.wb_entity_name + " has been set")

            return True
        except Exception as e:
            _LOGGER.error("Error updating the web bulb temperature")
            _LOGGER.error(e)
            return False

    