'''Custom component for web bulb  temps'''

import logging
from multiprocessing.spawn import prepare
from homeassistant.const import EVENT_HOMEASSISTANT_START, EVENT_HOMEASSISTANT_STOP
from homeassistant.core import HomeAssistant
import homeassistant.helpers.config_validation as cv
from homeassistant.helpers.typing import ConfigType
from . import wetbulb_config
from homeassistant.const import CONF_NAME

_LOGGER = logging.getLogger(__name__)

DOMAIN = 'wetbulb'
CONF_TEMP_SENSOR = "temp_sensor"
CONF_RH_SENSOR = "rh_sensor"
CONF_NUMBER_OF_DIGITS = "number_of_digits"
CONF_UNIQUE_ID = "unique_id"
CONF_ENTITY_DESCRIPTION = "entity_description"

def setup(hass: HomeAssistant, config: ConfigType) -> bool:
    conf = config[DOMAIN]

    wbconfig = wetbulb_config.wb_config()
    wbconfig.domain = DOMAIN
    wbconfig.name = conf.get(CONF_NAME)
    wbconfig.temp_sensor = conf.get(CONF_TEMP_SENSOR)
    wbconfig.rh_sensor = conf.get(CONF_RH_SENSOR)
    wbconfig.number_of_digits = conf.get(CONF_NUMBER_OF_DIGITS)
    wbconfig.unique_id = conf.get(CONF_UNIQUE_ID)
    wbconfig.entity_description = conf.get(CONF_ENTITY_DESCRIPTION)

    hass.data[DOMAIN] = wbconfig       

    return True 
  

