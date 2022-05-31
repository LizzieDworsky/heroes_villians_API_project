from django.urls import path
from . import views

urlpatterns = [
    path('', views.supers_list),
    path('<int:pk>/', views.super_details),
    path('<int:pk>/supers', views.super_details),
]