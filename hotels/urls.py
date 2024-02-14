from django.urls import path
from .views import hotels_list

urlpatterns = [
    path('hotels/', hotels_list, name='hotels_list'),
]
