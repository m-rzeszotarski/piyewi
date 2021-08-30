from django.urls import path
from . import views 

urlpatterns = [
    path('', views.glowna, name='glowna'),
    path('yerba_list', views.yerba_list, name='yerba_list')
]