from django.urls import path
from .views import Login, Logout, RegisterView
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path("login/", csrf_exempt(Login.as_view()), name='login'),
    path("register/", csrf_exempt(RegisterView.as_view()), name='register'),
    path("logout/", Logout.as_view(), name='logout'),
]
