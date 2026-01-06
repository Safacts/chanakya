# J:\chanakya\fee\urls.py
from django.urls import path
from . import views

# This variable MUST be named exactly 'urlpatterns' (no underscores, plural)
urlpatterns = [
    path('', views.fee_index, name='fee_index'),
]