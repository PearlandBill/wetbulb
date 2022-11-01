'''Custom component for web bulb temps'''
from homeassistant import config_entries, core
from .const import DOMAIN
from homeassistant.const import CONF_SENSOR
  
async def async_setup_entry(
    hass: core.HomeAssistant,
    entry: config_entries.ConfigEntry
) -> bool:
    """Set up platform from a config entry"""
    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = entry.data

    # Forward the setup to the sensor platform
    hass.async_create_task(
        hass.config_entries.async_forward_entry_setup(entry, CONF_SENSOR)
    )

    return True