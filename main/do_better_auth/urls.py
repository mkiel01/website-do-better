from django.urls import path
from .views import CustomLoginView, RegisterPage
from django.contrib.auth.views import LogoutView #we dont need a seperate view fun only build in
 
urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
]