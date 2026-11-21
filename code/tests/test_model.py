from src.model import Forecast
    
def test_for_model():
    title = {
        'address': 'Minsk',
        'latitude': 11,
        'longitude': 12,
        'timezone' : 'utc',
        'curr_temperature' : '12',
        'condition' : 'clear'
    }
    
    days = []
    hours = []
    
    forecast = Forecast(title=title, clear_days=days, clear_hours=hours)
    
    result = forecast.get_obj()
    
    assert result == (
         'Minsk',
        [11, 12],
        'utc',
        '12',
        'clear',
        [],
        []
    )