from src.adapter import clear_days, clear_hours, clear_title
import json
from pathlib import Path

file_path = Path(__file__).resolve().parent.parent / 'src' /'for_tests.json'

with open (file_path, 'r', encoding='utf-8') as file: 
    data = json.load(file)


def test_clear_title():
    obj = {
    'address': "London,UK",
    'latitude': 51.5064,
    'longitude': -0.12719,
    'timezone': "Europe/London",
    'curr_temperature': 4.8,
    'condition': 'Partially cloudy',
    } 
    
    clear_obj = clear_title(data, day=1)
    
    assert obj == clear_obj


def test_clear_days():
    days = [{'datetime':"2026-11-20",
               'tempmax':9.8,
                'tempmin':4.0,
                'temp':6.6,
                'humidity':89.3,
                'windspeed':17.3,
                'conditions':'Partially cloudy'},
            ]
    
    cleardays = clear_days(data)
    
    assert days == [cleardays[0]]
    
def test_clear_hours():
    hours = [{'datetime': '00:00:00',
           'temp': 6.1,
           'humidity': 93.31,
           'pressure': 995.0,
           'windspeed': 5.4,
           'conditions': 'Overcast'
            },
            {
           'datetime': '01:00:00',
           'temp': 6.0,
           'humidity': 94.48,
           'pressure': 995.0,
           'windspeed': 3.6,
           'conditions': 'Overcast'}
    ]
    
    clearhours = clear_hours(data, '2026-11-20')
    
    
    assert hours == clearhours[:2]