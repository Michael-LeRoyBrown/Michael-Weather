from django.urls import path
from . import views


app_name = 'weather'

urlpatterns = [
    # Home page.
    path('', views.index, name='index'),
    # Search page.
    path('search/', views.search, name='search'),
    #Delete city.
    path('delete/<city_name>/', views.delete_city, name='delete_city'),
    #Deelet all cities.
    path('deleteall/', views.delete_all, name='delete_all'),
]       