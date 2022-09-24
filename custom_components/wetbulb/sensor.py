from homeassistant.const import CONF_SWITCHES
from . import wetbulb_entity
import logging

_LOGGER = logging.getLogger(__name__)

DOMAIN = 'wetbulb'


def setup_platform(hass, config, add_entities, discovery_info=None):
    config = hass.data[DOMAIN]

    _LOGGER.error("setting up platform")

    #wetbulbs = config.get(CONF_SWITCHES)
    devices = []
    #for dev_name, properties in config.switches.items():

    wb = wetbulb_entity.WetBulbEntity(hass, 
        "Wet Bulb", 
        "sensor.khou_temperature", 
        "sensor.khou_relative_humidity", 
        "sensor.wb_outdoors")

    
    devices.append(wb)
    
    add_entities(devices)

