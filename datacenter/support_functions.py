import datetime
import django


def get_duration(visit):
    entered_at_time = django.utils.timezone.localtime(visit.entered_at)
    leaved_at_time = django.utils.timezone.localtime(visit.leaved_at)
    current_time = django.utils.timezone.localtime()

    if not visit.leaved_at:
        delta_time = current_time - entered_at_time
    else:
        delta_time = leaved_at_time - entered_at_time
        
    return round(delta_time.total_seconds())


def get_format_duration(duration):
    seconds_in_hour = 3600
    seconds_in_minute = 60
    hours, remains = divmod(duration, seconds_in_hour)
    minutes, seconds = divmod(remains, seconds_in_minute)
    
    return f"{hours:02d} часов, {minutes:02d} минут, {seconds:02d} секунд"


def is_visit_long(visit, minutes=60):
    suspect_time_seconds = minutes * 60
    visit_duration = get_duration(visit)
    
    return visit_duration > suspect_time_seconds
