def clear_title(json, day=None):
    current = json['days'][day] or json.get('currentConditions')
    
    return {
      'address': json['address'],
      'latitude': json['latitude'],
      'longitude': json['longitude'],
      'timezone': json['timezone'],
      'curr_temperature': current['temp'],
      'condition': current['conditions'],
  }
    
    
def clear_days(json):
    days = []
    for day in json['days']:
        curr_day = {'datetime':day['datetime'],
                   'tempmax':day['tempmax'],
                    'tempmin':day['tempmin'],
                    'temp':day['temp'],
                    'humidity':day['humidity'],
                    'windspeed':day['windspeed'],
                    'conditions':day['conditions']}
        days.append(curr_day)
    return days


def clear_hours(json, target_date): #'2026-11-20'    
    hours = []
    for day in json.get('days', []):
        if day['datetime'] == target_date:
            for hour in day.get('hours', []):
                clear_hour = {'datetime':hour['datetime'],
                              'temp':hour['temp'],
                              'humidity':hour['humidity'],
                              'pressure':hour['pressure'],
                              'windspeed':hour['windspeed'],
                              'conditions':hour['conditions']}
                hours.append(clear_hour)
    return hours