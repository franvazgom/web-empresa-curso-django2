from django.urls import path
from . import views
urlpatterns = [
    #path CORE    
    path('', views.contact, name='contact' ),
]