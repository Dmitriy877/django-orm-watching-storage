from django.db import models
import datetime
import django


def get_duration(visit):
    entered_at_time = django.utils.timezone.localtime(visit.entered_at)
    leaved_at_time = django.utils.timezone.localtime(visit.leaved_at)
    current_time = django.utils.timezone.localtime()

    if visit.leaved_at is None:
        delta_time = current_time - entered_at_time
    else:
        delta_time = leaved_at_time - entered_at_time
    return round(delta_time.total_seconds())


def get_format_duration(duration):
    return str(datetime.timedelta(seconds=duration))


def is_visit_long(visit, minutes=60):
    suspect_time_seconds = minutes * 60
    visit_duration = get_duration(visit)

    if visit_duration < suspect_time_seconds:
        return False
    else:
        return True


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )
