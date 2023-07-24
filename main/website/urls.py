from django.urls import path, include
from . import views


urlpatterns = [
  path('auth/', include('do_better_auth.urls')),
  path('dairy/', include('dairy.urls')),

  path('', views.home, name='home'),
  path('calendar', views.calendar, name="calendar"),
  path('contact', views.contact, name="contact"),
  path('introduction', views.introduction, name="introduction"),
  path('program', views.program, name="program"),
  path('hours', views.hours, name="hours"),
  path('your-name/', views.minutes, name="your-name"),
  
]