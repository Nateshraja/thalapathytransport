from django.urls import path
from . import views

urlpatterns = [
    path('trips/', views.trip_list, name='trip_list'),
    path('trips/add/', views.trip_entry_view, name='trip_entry'),
    path('trips/<int:pk>/pdf/', views.trip_pdf, name='trip_pdf'),
    path('trips/<int:pk>/send-whatsapp/', views.send_whatsapp, name='send_whatsapp'),
]
