from django.urls import path
from . import views

urlpatterns = [
    path('index', views.Index, name='index'),
    path('find', views.GetFind, name='find'),
    path('add', views.GetAdd, name='add'),
    path('search', views.GetSearch, name='search'),
    path('modify', views.GetModify, name='modify'),
    path('delete', views.GetDelete, name='delete')
]