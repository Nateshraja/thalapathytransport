from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect

def redirect_to_admin(request):
    return redirect('/admin/login/')

urlpatterns = [
    path('', redirect_to_admin, name='redirect_to_admin'),
    path('trips/', views.trip_list, name='trip_list'),
    path('trips/add/', views.trip_entry_view, name='trip_entry'),
    path('trips/<int:pk>/pdf/', views.trip_pdf, name='trip_pdf'),
    path('trips/<int:pk>/send-whatsapp/', views.send_whatsapp, name='send_whatsapp'),
]
