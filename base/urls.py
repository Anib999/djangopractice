from django.urls import path
from . import views

urlpatterns = [
    path('', views.viewAllRoutes, name="viewAllRoutes")
]