from django.urls import path

from . import views
app_name = 'entry'
urlpatterns = [
    path('', views.index, name='index'),
    path('checkin/', views.guest_entry, name='guest_form'),
    path('host/', views.host_entry, name='host_form'),
    path('checkout/', views.guest_checkout, name='guest_checkout'),
]
