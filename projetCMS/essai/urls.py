from django.contrib import admin
from django.urls import path

from demineur.views import vue_partie

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', vue_partie),
]
