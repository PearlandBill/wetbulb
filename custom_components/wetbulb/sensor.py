from numpy import number
from . import wetbulb_entity
import logging
import voluptuous as vol
import homeassistant.helpers.config_validation as cv
from homeassistant.components.sensor import SensorEntity, PLATFORM_SCHEMA
from homeassistant.const import CONF_NAME, CONF_SENSORS, CONF_SWITCHES

_LOGGER = logging.getLogger(__name__)

DOMAIN = 'wetbulb'
CONF_FRIENDLY_NAME = "friendly_name"
CONF_WB_ENTITY = "wetbulb_entity"
CONF_TEMP_ENTITY = "temp_sensor"
CONF_RH_ENTITY = "rh_sensor"
CONF_UOM = 'unit_of_measure'
CONF_DIGITS = 'number_of_digits'

WETBULB_SCHEMA = vol.Schema(
    {
        vol.Required(CONF_FRIENDLY_NAME): vol.All(cv.ensure_list_csv, [cv.string]),
        vol.Required(CONF_TEMP_ENTITY): vol.All(cv.ensure_list_csv, [cv.string]),
        vol.Required(CONF_RH_ENTITY): vol.All(cv.ensure_list_csv, [cv.string]),
        vol.Required(CONF_WB_ENTITY): vol.All(cv.ensure_list_csv, [cv.string]),
    }
)

_LOGGER.error(WETBULB_SCHEMA)

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Required(CONF_SENSORS): vol.Schema({cv.string: WETBULB_SCHEMA}),
    }
)
 


def setup_platform(hass, config, add_entities, discovery_info=None):
    #Get the config data
    wb_config = hass.data[DOMAIN]
    #unit_of_measure = wb_config[CONF_UOM]
    #number_of_digits = wb_config[CONF_DIGITS]

    #_LOGGER.error("setting up platform")

    wetbulbs = config.get(CONF_SENSORS)
    switches = config.get(CONF_SWITCHES)
    devices = []
    for dev_name, properties in wetbulbs.items():

        #_LOGGER.error("Name entity = " + properties.get(CONF_FRIENDLY_NAME)[0])
        #_LOGGER.error("Temp entity = " + properties.get(CONF_TEMP_ENTITY)[0])
        #_LOGGER.error("RH entity = " + properties.get(CONF_RH_ENTITY)[0])
        #_LOGGER.error("WB entity = " + properties.get(CONF_WB_ENTITY)[0])

        wb = wetbulb_entity.WetBulbEntity(hass,
            properties.get(CONF_NAME, dev_name)[0],
            properties.get(CONF_TEMP_ENTITY)[0],
            properties.get(CONF_RH_ENTITY)[0],
            properties.get(CONF_WB_ENTITY)[0],
            wb_config
        )
    
        devices.append(wb)

        #wb.update()
    
    add_entities(devices)

