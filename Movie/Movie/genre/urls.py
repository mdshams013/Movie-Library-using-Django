from django.urls import path
from . import views

app_name = 'genre'

urlpatterns = [
    path('add/', views.new, name='add'),
    path('<int:pk>/', views.detail, name='detail')
    
]