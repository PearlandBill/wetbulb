'''Custom component for web bulb  temps'''

import logging

_LOGGER = logging.getLogger(__name__)

DOMAIN = 'wetbulb'
CONF_UOM = 'unit_of_measure'
CONF_OUTDOOR_TEMP_ENTITY = 'outdoor_temp_entity'
CONF_INDOOR_TEMP_ENTITY = 'indoor_temp_entity'
CONF_OUTDOOR_RH_ENTITY = 'outdoor_rh_entity'
CONF_INDOOR_RH_ENTITY = 'indoor_rh_entity'

def setup(hass, config):
    conf = config[DOMAIN]
    unit_of_measure = config[CONF_UOM]
    outdoor_temp_entity = config[CONF_OUTDOOR_TEMP_ENTITY]
    indoor_temp_entity = config[CONF_INDOOR_TEMP_ENTITY]    
    outdoor_rh_entity = config[CONF_OUTDOOR_RH_ENTITY]
    indoor_rh_entity = config[CONF_INDOOR_RH_ENTITY]        

    return True 
     

