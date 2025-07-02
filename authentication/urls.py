from django.urls import path
from .views import RegisterView, LogoutView, MeView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('me/', MeView.as_view(), name='auth-me'),
]