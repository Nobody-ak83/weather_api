from src.adapter import clear_days, clear_title, clear_hours
from src.model import Forecast
from src.uni import get_response



def get_forecast():
    raw_data = get_response()
    title = clear_title(raw_data, day=0)
    days = clear_days(raw_data)
    hours = clear_hours(raw_data, '2026-11-21')
    
    forecast = Forecast(title=title, clear_days=days, clear_hours=hours)
    
    return forecast