from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('sign/', views.sign, name='sign'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('reset_password/', views.reset_password, name='reset_password'),
    path('recommendations/', views.recommendations, name='recommendations'),
    path('cart/', views.cart_view, name='cart'),  # Removed duplicate
    path('userprofile/', views.user_profile, name='userprofile'),
    path('about/', views.about, name='about'),
    path('help/', views.about, name='help'),
    path('terms/', views.about, name='terms'),
    path('contact/', views.about, name='contact'),
    path('notifications/', views.about, name='notifications'),
    path('logout/', views.about, name='logout'),
    path('search/', views.about, name='search'),
    path('favorites/', views.about, name='favorites'),
    path('viewall/', views.view_all, name='viewall'),
    path('science/', views.view_all, name='science'),
    path('fiction/', views.view_all, name='fiction'),
    path('history/', views.view_all, name='history'),
    path('technology/', views.view_all, name='technology'),
    path('payment/', views.about, name='payment'),
]