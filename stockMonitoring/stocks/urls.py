from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('index/', views.index, name='index'),
    path('api/stock-history/', views.get_stock_history, name='stock_history'),
    
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register')
]