from django.urls import path
from . import views

urlpatterns = [
    path('new/', views.new_good, name='new_good'),
    path('<int:uprice>/', views.main, name= 'all_goods'),
]