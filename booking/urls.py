from django.urls import path
from. import views

urlpatterns = [

    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('contact/', views.contact, name='contact'),
    path('bookings/', views.bookings, name='bookings'),
    path('confirmation/', views.confirmation, name='confirmation'),

]
