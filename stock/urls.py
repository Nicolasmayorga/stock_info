from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('stock_info/', views.stock_info, name='stock_info'),
]