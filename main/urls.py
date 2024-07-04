from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('accounts/', include('django.contrib.auth.urls')),  # for login
    path('register/', views.register, name='register'),  # for registration
]
