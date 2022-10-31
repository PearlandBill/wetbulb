from homeassistant import config_entries, core
import voluptuous as vol
import logging
from typing import Any, Dict, Optional
import homeassistant.helpers.config_validation as cv
from .const import DOMAIN, CONF_TEMP_ENTITY, CONF_RH_ENTITY, CONF_NUM_DIGITS
import homeassistant.helpers.config_validation as cv
from homeassistant.helpers.entity_registry import (
    async_entries_for_config_entry,
    async_get_registry,
)
from homeassistant.core import callback
from homeassistant.helpers.aiohttp_client import async_get_clientsession

SENSOR_SCHEMA = vol.Schema(
    {
        vol.Required(CONF_TEMP_ENTITY): cv.string,
        vol.Required(CONF_RH_ENTITY): cv.string,
        vol.Required(CONF_NUM_DIGITS): cv.positive_int,
    }
)

_LOGGER = logging.getLogger(__name__)

async def validate_wetbulb(temp_sensor: str, rh_sensor: str, number_of_decimals: str, hass: core.HassJob) -> None:
    """Raise a ValueError if either sensor does not exist."""
    if number_of_decimals is None:
        raise ValueError

    try:
        temp_num = float(number_of_decimals)
    except:
        raise ValueError

class WetBulbConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Wet Bulb Custom Configuration"""

    data: Optional[Dict[str, Any]]

    async def async_setup_user(self, user_input: Optional[Dict[str, Any]] = None):
        """Invoked when a user initiates a flow via the user interface"""
        errors: Dict[str, str] = {}

        if user_input is not None:
            try:
                await validate_wetbulb(user_input[CONF_TEMP_ENTITY], user_input[CONF_RH_ENTITY], user_input[CONF_NUM_DIGITS])
            except:
                raise ValueError

            if not errors:
                self.data = user_input

                if user_input.get("add_another", False):
                    return await self.async_step_init
            
            return await self.async_create_entry(title="WetBulb Custom", data=self.data)

        return self.async_show_form(
            step_id = "user", data_schema=SENSOR_SCHEMA, errors=errors
        )
    #End of async_setup_user
