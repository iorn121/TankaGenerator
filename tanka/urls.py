from django.urls import path
from . import views

app_name='tanka'
urlpatterns = [
    path('index/', views.IndexView,name='index'),
]