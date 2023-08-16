
from django.urls import path
from .views import register_view, login_view, logout_view

app_name = 'authentication'
urlpatterns = [
    path('sign-up/', register_view, name="sign.up"),
    path('sign-in/', login_view, name="sign.in"),
    path('sign-out/', logout_view, name="sign.out"),
]
