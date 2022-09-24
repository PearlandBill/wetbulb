''' Wetbulb entity class'''
from homeassistant.const import EVENT_HOMEASSISTANT_START, EVENT_HOMEASSISTANT_STOP
import homeassistant.helpers.config_validation as cv
import voluptuous as vol
from homeassistant.components.sensor import SensorEntity
from . import calculator

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
        #get the temperature
        temp_str = self.hass.states.get(self.temp_entity)
        rh_str = self.hass.states.get(self.rh_entity)

        temp = 0
        rh = 0

        # Validate values
        try:
            temp = float(temp_str)
            rh = int(rh_str)
        except:
            return False

        # find wet bulb
        wb = calculator.calcwb(temp, rh, 2, 'F')

        # set state
        self.hass.states.set(self.wetbulb_entity, wb)

        return True

    