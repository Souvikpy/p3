from django.urls import path
from myapp01 import views

app_name='myapp01'

urlpatterns = [
    path('trails/',views.trails,name='trails'),
    path ('profile/',views.profile,name='profile'),
]
