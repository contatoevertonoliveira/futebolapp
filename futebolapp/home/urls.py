from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView),
    path('page/<int:page>/', views.HomePageView),
]