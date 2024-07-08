from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_dashboard, name='user_dashboard'),
    path('tasks/', views.tasks, name='tasks'),
    path('profile/', views.profile, name='profile'),
    path('settings/', views.settings, name='settings'),
    path('purchase_account/', views.purchase_account, name='purchase_account'),
]
