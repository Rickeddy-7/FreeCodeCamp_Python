
def add_time(start,duration,weekday=''):
    """add the duration time to the start time and return the result"""

    dur_nums, start_nums = duration.split(':'), start.split(':')
    if weekday != '': w_day = weekday.capitalize() 
    meridiem = start_nums[1][-2:]
    days_count = 0

    x = int(dur_nums[0])
    if x > 24:
        days_count += x // 24
        dur_nums[0] = x % 24
    
    time_mins = int(start_nums[1][:2]) + int(dur_nums[1])
    time_hrs = int(start_nums[0]) + int(dur_nums[0])
    
    if time_mins > 60:
    # Calculate number of hours and remaining minutes
        time_hrs += time_mins // 60
        time_mins = time_mins % 60
    
    # Calculate number of days and remaining hours
    days_count, time_hrs = get_num_days(days_count,time_hrs,meridiem)
    
    # determine the proper meridiem
    new_mrd = get_meridiem(start_nums,dur_nums)
    
    if weekday != '':
        if days_count == 0 or days_count == 7:
            new_time = f'{time_hrs}:{time_mins:02} {new_mrd}, {w_day}'
        elif days_count == 1:
            wd = get_weekday(w_day,days_count)
            new_time = f'{time_hrs}:{time_mins:02} {new_mrd}, {wd} (next day)'
        else:
            wd = get_weekday(w_day,days_count)
            new_time = f'{time_hrs}:{time_mins:02} {new_mrd}, {wd} ({days_count} days later)'

    else: # weekday not given
        if days_count == 0:
            new_time = f'{time_hrs}:{time_mins:02} {new_mrd}'
        elif days_count == 1:
            new_time = f'{time_hrs}:{time_mins:02} {new_mrd} (next day)'
        else:
            new_time = f'{time_hrs}:{time_mins:02} {new_mrd} ({days_count} days later)'

    return new_time


def get_num_days(days,hours,meridiem):
    """returns the proper number of days and remaining hours"""

    if hours % 24 == 0:
        days += (hours // 24)
        hours = 12
    else:
        if meridiem == 'PM' and hours > 12:
            if (hours % 12) == 0:
                days += (hours // 12) - 1
            else: days += (hours // 12)

        else: days += (hours // 24)
        
        hours = hours % 12
        if hours == 0: hours = 12

    return days,hours


def get_weekday(day,n):
    """return the weekday after adding (n) days starting from (day)"""
    
    if n >= 7: n = n % 7
    if n == 0: return day
    
    index, weekdays = 0, ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    for i in range(7):
        if day == weekdays[i]:
            index = i
            break
    indx = index + n
    if indx == 7: indx = 0

    return weekdays[indx]


def get_meridiem(start:list, duration:list):
    """returns the proper meridiem"""

    days, meridiem = 0, start[1][-2:]
    time_hrs = int(start[0]) + int(duration[0])
    time_mins =  int(start[1][:2]) + int(duration[1])

    if time_mins > 60: time_hrs += time_mins // 60
    days += time_hrs // 12

    if days % 2 == 0: new_mrd = meridiem
    else:
        if meridiem == 'AM': new_mrd = 'PM'
        else: new_mrd = 'AM'

    return new_mrd


# print(add_time("8:16 PM", "466:02", "tuesday"))
# "6:18 AM, Monday (20 days later)"
