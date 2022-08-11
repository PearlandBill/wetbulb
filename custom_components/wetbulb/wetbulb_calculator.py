class WetBulbCalculator(SensorEntity):
    def __init__(self, name, friendly_name):
        self.name = name
        self.friently_name = friendly_name

    @property
    def should_poll(self):
        return False

    @property
    def name(self):
        return self.name

    @property
    def friendly_name(self):
        return self.friendly_name

    def calc_wb():
        return False
