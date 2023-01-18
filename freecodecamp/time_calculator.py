def add_time(start, end, day=False):
    expected = 0    
    periods = ['AM', 'PM']
    start_hour, start_minute, start_period = *start.split()[0].split(":"), start.split()[1]
    end_hour, end_minute = end.split(":")

    if not start_hour.isdigit() or not start_hour.isdigit() or start_period not in periods:
        return "Error: Invalid time had been given"

    expected = (int(start_hour) * 60 + int(start_minute)) + (int(end_hour) * 60 + int(end_minute))
    expected_hour = round(expected/60)
    expected_minute = expected%60


    return f'{expected_hour}:{expected_minute} {start_period}'