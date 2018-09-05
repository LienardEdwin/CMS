from django.contrib import admin
from .models import Partie, Mine


@admin.register(Partie)
class PartieAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'nom', 'dateheure_debut', 'dateheure_modification']
    list_editable = ['nom']
    date_hierarchy = 'dateheure_debut'


@admin.register(Mine)
class MineAdmin(admin.ModelAdmin):
    list_display = ['id', 'partie', 'position_x', 'position_y']
    list_editable = ['partie', 'position_x', 'position_y']

