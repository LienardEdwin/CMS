from django.shortcuts import render_to_response
from .logique_magique import get_table
from .models import Partie, Mine

def vue_partie(request):
    partie, created = Partie.objects.get_or_create(nom='partie de test')
    if created:
        for i in range(20):
            Mine.objects.create(partie=partie)
    return render_to_response('partie.html', {
        'partie': partie,
        'tableau': get_table(partie.mines.all()),
    })
