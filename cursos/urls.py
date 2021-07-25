from django.urls import path
from . import views
                    
urlpatterns = [
    path('', views.index),
    path('course/<int:id>/delete', views.delete)
]