def add_time(start, end, day = None):    
    periods = ['AM', 'PM']
    start_hour, start_minute, start_period = *start.split()[0].split(":"), start.split()[1]
    start_hour = int(start_hour) + 12 if start_period == 'PM' else int(start_hour)
    end_hour, end_minute = end.split(":")
    days = [
        'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'
    ]

    if not str(start_hour).isdigit() or not str(start_hour).isdigit() or start_period not in periods:
        return "Error: Invalid time had been given"

    #get the expected minute in time by getting the remain of division by 60 
    expected_minute = (int(start_minute) + int(end_minute)) % 60

    #get estimated hour
    expected_hour = ((int(start_minute) + int(end_minute))//60 + start_hour + int(end_hour))%24
    
    #determining the period according to expected hour
    expected_period = 'AM' if expected_hour < 12 else 'PM'
    
    #change the expected hour to 12 if expected hour is 0 (12 hours format)
    expected_hour = 12 if expected_hour == 0 else expected_hour
    expected_hour = expected_hour - 12 if expected_hour>12 else expected_hour

    #count days spent
    day_count = ((int(start_minute) + int(end_minute))//60 + start_hour + int(end_hour))//24
    if day_count == 0:
        expected_day_count = ''
    elif day_count == 1:
        expected_day_count = ' (next day)'
    else:
        expected_day_count = f' ({day_count} days later)'
    
    #get name of the day
    if day:
        current_day_index = days.index(day.lower())
        expected_day = days[(current_day_index + day_count)%7][0].upper() + days[(current_day_index + day_count)%7][1:]
        new_time = f'{expected_hour}:{"0" + str(expected_minute) if expected_minute//10 == 0 else expected_minute} {expected_period}, {expected_day}{expected_day_count}'
    else:
        new_time = f'{expected_hour}:{"0" + str(expected_minute) if expected_minute//10 == 0 else expected_minute} {expected_period}{expected_day_count}'
    return new_time