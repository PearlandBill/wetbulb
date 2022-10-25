from . import wetbulb_entity
import logging
import voluptuous as vol
import homeassistant.helpers.config_validation as cv
from homeassistant.components.sensor import PLATFORM_SCHEMA
from homeassistant.const import CONF_SENSORS

DOMAIN = 'wetbulb'
CONF_TEMP_ENTITY = "temp_sensor"
CONF_RH_ENTITY = "rh_sensor"
CONF_NUM_DIGITS = "number_of_decimals"

SENSOR_SCHEMA = vol.Schema(
    {
        vol.Required(CONF_TEMP_ENTITY): vol.All(cv.ensure_list_csv, [cv.string]),
        vol.Required(CONF_RH_ENTITY): vol.All(cv.ensure_list_csv, [cv.string]),
        vol.Required(CONF_NUM_DIGITS): vol.All(cv.ensure_list_csv, [cv.positive_int])
    }
)

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
	{
		vol.Required(CONF_SENSORS): vol.Schema({cv.string: SENSOR_SCHEMA}),
	}
)

def setup_platform(hass, config, add_entities, discovery_info=None):
    #Get the config data
    sensors = config.get(CONF_SENSORS)

    devices = []
    for dev_name, properties in sensors.items():
        wb = wetbulb_entity.WetBulbEntity(hass, 
            properties.get(CONF_TEMP_ENTITY)[0],
            properties.get(CONF_RH_ENTITY)[0],
            properties.get(CONF_NUM_DIGITS)[0]
            )
        wb._attr_name = dev_name
        
        devices.append(wb)
    
    add_entities(devices)

