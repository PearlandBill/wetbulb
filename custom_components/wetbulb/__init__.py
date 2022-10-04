'''Custom component for web bulb  temps'''

import logging
from multiprocessing.spawn import prepare
from homeassistant.const import EVENT_HOMEASSISTANT_START, EVENT_HOMEASSISTANT_STOP
import homeassistant.helpers.config_validation as cv
#import voluptuous as vol
#import threading
from . import wetbulb_config

_LOGGER = logging.getLogger(__name__)

DOMAIN = 'wetbulb'
CONF_UOM = 'unit_of_measure'
CONF_DIGITS = 'number_of_digits'

def setup(hass, config):
    conf = config[DOMAIN]
    wbconfig = wetbulb_config.wb_config()
    wbconfig.unit_of_measure = conf[CONF_UOM]
    wbconfig.number_of_digits = conf[CONF_DIGITS]

    #def cleanup(event):
    #    conf.cleanup()

    #def prepare(event):
    #    conf.prepare
    #    conf.startReceivingThread()
    #    hass.bus.listen_once(EVENT_HOMEASSISTANT_STOP, cleanup)

    #hass.bus.listen_once(EVENT_HOMEASSISTANT_START, prepare)
    hass.data[DOMAIN] = wbconfig       

    return True 
  

