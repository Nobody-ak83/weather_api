class Forecast:
    def __init__(self, title: dict, clear_days:list, clear_hours: list):
        self.address = title['address']
        self.coordinates = [title['latitude'], title['longitude']]
        self.timezone = title['timezone']
        self.curr_temperature = title['curr_temperature']
        self.condition = title['condition']
        self.days = clear_days
        self.hours = clear_hours

           
    def get_obj(self):
        return (
            self.address,
            self.coordinates,
            self.timezone,
            self.curr_temperature,
            self.condition,
            self.days,
            self.hours
        )
    
