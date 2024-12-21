from django.urls import path
from .views import viev1, viev2, viev3, viev4, viev5, viev6, viev7, viev8, viev9, viev10

urlpatterns = [
    path('', viev1, name='home'),
    path('viev2/', viev2, name='viev2'),
    path('viev3/', viev3, name='viev3'),
    path('viev4/', viev4, name='viev4'),
    path('viev5/', viev5, name='viev5'),
    path('viev6/', viev6, name='viev6'),
    path('viev7/', viev7, name='viev7'),
    path('viev8/', viev8, name='viev8'),
    path('viev9/', viev9, name='viev9'),
    path('viev10/', viev10, name='viev10'),
]
