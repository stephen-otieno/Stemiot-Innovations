from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='homepage'),
    path('clients/', views.client_details, name='clients'),
    path('clients_data/', views.clients_table, name='clients_data'),
]