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
CONF_OUTDOOR_TEMP_ENTITY = 'outdoor_temp_entity'
CONF_INDOOR_TEMP_ENTITY = 'indoor_temp_entity'
CONF_OUTDOOR_RH_ENTITY = 'outdoor_rh_entity'
CONF_INDOOR_RH_ENTITY = 'indoor_rh_entity'

wbconfig = wetbulb_config.wb_config()

def setup(hass, config):
    conf = config[DOMAIN]
    wbconfig.unit_of_measure = conf[CONF_UOM]
    wbconfig.outdoor_temp_entity = conf[CONF_OUTDOOR_TEMP_ENTITY]
    wbconfig.indoor_temp_entity = conf[CONF_INDOOR_TEMP_ENTITY]    
    wbconfig.outdoor_rh_entity = conf[CONF_OUTDOOR_RH_ENTITY]
    wbconfig.indoor_rh_entity = conf[CONF_INDOOR_RH_ENTITY] 

    #def cleanup(event):
    #    conf.cleanup()

    #def prepare(event):
    #    conf.prepare
    #    conf.startReceivingThread()
    #    hass.bus.listen_once(EVENT_HOMEASSISTANT_STOP, cleanup)

    #hass.bus.listen_once(EVENT_HOMEASSISTANT_START, prepare)
    hass.data[DOMAIN] = wbconfig       

    return True 
  

