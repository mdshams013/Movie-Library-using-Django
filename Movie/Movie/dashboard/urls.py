from django.urls import path
from . import views
from dashboard.views import add_to_list,list

app_name = 'dashboard'

urlpatterns = [
    path('add-to-list/<int:pk>/' , add_to_list, name='add_to_list'),
    path('list/', list , name = 'list'),
]