from django.urls import path
from .views import *


app_name = 'resume'
urlpatterns = [
    path('', home_1_view, name='home_1'),
    path('contact/', contact_view, name='contact'),
]
