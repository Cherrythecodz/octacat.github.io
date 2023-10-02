from django.urls import path
from .views import create_order, register, AdminDashboard

urlpatterns = [
    path('frontend\AdminDashboard.html', AdminDashboard, name='AdminDashboard'),
    path('frontend\src\Pages\Register.js', register, name='Register' ),
]
