from django.urls import path
from . import views

urlpatterns = [
    path('<int:uprice>/', views.main, name= 'all_goods')
]