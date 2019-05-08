from django.urls import path
from .import views
urlpatterns = [
    #path CORE    
    path('', views.services, name='services' ),    
]