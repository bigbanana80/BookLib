from django.urls import path,include
from .views import *

app_name = 'BookLib'

urlpatterns = [
    path('', index.as_view(), name='index'),
]
