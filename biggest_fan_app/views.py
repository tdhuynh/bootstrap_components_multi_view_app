from django.shortcuts import render
from biggest_fan_app.models import Faction


def index_view(request):
    context = {
        "all_factions": Faction.objects.all(),
    }
    return render(request, 'index.html', context)


def faction_view(request, f_id):
    context = {
        "all_factions": Faction.objects.all(),
        "faction": Faction.objects.get(id=f_id)
    }
    return render(request, 'faction.html', context)

def about_me_view(request):
    context = {
        "all_factions": Faction.objects.all(),

    }
    return render(request, 'about_me.html', context)
