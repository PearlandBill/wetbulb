''' Data class for wet bulb configuration'''
from dataclasses import dataclass

@dataclass
class wb_config:
    unit_of_measure: str = None
    number_of_digits: int = None


