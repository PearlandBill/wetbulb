from numpy import number
from . import wetbulb_entity
import logging
import voluptuous as vol
import homeassistant.helpers.config_validation as cv
from homeassistant.components.sensor import SensorEntity, PLATFORM_SCHEMA
from homeassistant.const import CONF_NAME, CONF_SENSORS, CONF_SWITCHES

_LOGGER = logging.getLogger(__name__)
DOMAIN = 'wetbulb'

def setup_platform(hass, config, add_entities, discovery_info=None):
    #Get the config data
    wb_config = hass.data[DOMAIN]

    #_LOGGER.error("setting up platform")
    devices = []

    wb = wetbulb_entity.WetBulbEntity(hass, wb_config)

    devices.append(wb)
    
    add_entities(devices)

