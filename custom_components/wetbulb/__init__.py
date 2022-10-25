'''Custom component for web bulb  temps'''

import logging
from multiprocessing.spawn import prepare
from homeassistant.const import EVENT_HOMEASSISTANT_START, EVENT_HOMEASSISTANT_STOP
from homeassistant.core import HomeAssistant
import homeassistant.helpers.config_validation as cv
from homeassistant.helpers.typing import ConfigType
import voluptuous as vol
from . import wetbulb_config
from homeassistant.const import CONF_NAME

_LOGGER = logging.getLogger(__name__)

DOMAIN = 'wetbulb'

def setup(hass: HomeAssistant, config: ConfigType) -> bool:
    conf = config[DOMAIN]

    return True 
  

