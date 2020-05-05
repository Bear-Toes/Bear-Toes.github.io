from django.urls import path, include
from . import views

urlpatterns = [
    # Default View
    path('', views.index, name='index'),

    # /Student/
    path('<str:name>/', views.detail, name='detail')
]