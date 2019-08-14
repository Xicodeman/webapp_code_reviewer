from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='codereviewerapp-home'),
    path('about/', views.about, name='codereviewerapp-about'),
]
