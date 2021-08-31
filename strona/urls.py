from django.urls import path
from . import views 

urlpatterns = [
    path('', views.glowna, name='glowna'),
    path('yerba_list', views.yerba_list, name='yerba_list'),
    path('yerba/<int:pk>/', views.yerba_detail, name='yerba_detail'),
    path('yerba/new', views.yerba_new, name='yerba_new'),
    path('yerba/<int:pk>/edit/', views.yerba_edit, name='yerba_edit'),
    path('yerba/<pk>/remove/', views.yerba_remove, name='yerba_remove'),
]