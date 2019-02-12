from django.urls import path
from . import views

urlpatterns = [
    path('index', views.Index, name='index'),
    path('', views.Home.as_view(), name='home'),
    path('find', views.FindRestaurant, name='find_restaurant'),
    path('reclamar-datos', views.reclama_datos, name='reclamar_datos'),
    path('add-restaurant', views.AddRestaurant, name='add_restaurant'),
    path('search', views.SearchRestaurant, name='search_restaurant'),
    path('modify-restaurant', views.ModifyRestaurant, name='modify_restaurant'),
    path('delete-restaurant', views.DeleteRestaurant, name='delete_restaurant'),
    path('list-plate', views.ListPlate, name='list_plate'),
    path('add-plate', views.AddPlate, name='add_plate'),
    path('modify-plate', views.ModifyPlate, name='modify_plate'),
    path('delete-plate', views.DeletePlate, name='delete_plate'),
]