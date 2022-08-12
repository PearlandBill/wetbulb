''' Data class for wet bulb configuration'''
from dataclasses import dataclass

@dataclass
class wb_config:
    unit_of_measure: str = ''
    outdoor_temp_entity: str = ''
    outdoor_rh_entity: str = ''
    indoor_temp_entity: str = ''
    indoor_rh_entity: str = ''

    def __str__(self):
        return f'''UOM = {self.unit_of_measure}
        Outdoor temp entity {self.outdoor_temp_entity}
        Outdoor rh entity {self.outdoor_rh_entity}
        Intdoor temp entity {self.indoor_temp_entity}
        Intdoor rh entity {self.indoor_rh_entity}'''

