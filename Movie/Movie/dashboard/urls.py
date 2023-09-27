from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('add_to_list/<uid>/', views.add_to_list, name='add_to_list')
]
