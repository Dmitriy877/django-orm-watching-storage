from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from .models import get_duration
from .models import get_format_duration


def storage_information_view(request):
    non_closed_visits = []
    visits_active = Visit.objects.filter(leaved_at=None)

    for visit in visits_active:
        owner = Passcard.objects.filter(owner_name=visit.passcard)[0]
        duration = get_format_duration(get_duration(visit))

        non_closed_visit = {
            'who_entered': owner.owner_name,
            'entered_at': visit.entered_at,
            'duration': duration,
        }
        non_closed_visits.append(non_closed_visit)

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
