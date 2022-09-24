''' Data class for wet bulb configuration'''
from dataclasses import dataclass

@dataclass
class wb_config:
    unit_of_measure: str = None
    outdoor_temp_entity: str = None
    outdoor_rh_entity: str = None
    indoor_temp_entity: str = None
    indoor_rh_entity: str = None

    def __str__(self):
        return f'''UOM = {self.unit_of_measure}
        Outdoor temp entity {self.outdoor_temp_entity}
        Outdoor rh entity {self.outdoor_rh_entity}
        Intdoor temp entity {self.indoor_temp_entity}
        Intdoor rh entity {self.indoor_rh_entity}'''

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'{self.unit_of_measure}, {self.outdoor_temp_entity}, '
                f'{self.outdoor_rh_entity}, {self.indoor_temp_entity}, '
                f'{self.indoor_rh_entity}')

    def is_valid(self):
        if self.unit_of_measure is not None and \
            self.outdoor_temp_entity is not None and \
            self.outdoor_rh_entity is not None and \
            self.indoor_temp_entity is not None and \
            self.indoor_rh_entity is not None:
            return True
        else:
            return False

