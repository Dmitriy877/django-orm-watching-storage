from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .support_functions import get_format_duration
from .support_functions import get_duration
from .support_functions import is_visit_long


def passcard_info_view(request, passcode):
   
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits_person = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []

    for visit in visits_person:
        duration = get_format_duration(get_duration(visit))
        this_passcard_visit = {
            'entered_at': visit.entered_at,
            'duration': duration,
            'is_strange': is_visit_long(visit)
        }
        this_passcard_visits.append(this_passcard_visit)

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
