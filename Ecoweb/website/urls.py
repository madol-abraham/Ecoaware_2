from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('donate/', views.donate, name='donate'),
    path('posts/', views.post_list, name='post_list'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('thank_you/', views.thank_you, name='thank_you'),
]
