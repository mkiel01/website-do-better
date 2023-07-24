from django.urls import path

from django.contrib.auth.views import LogoutView #we dont need a seperate view fun only build in
from . import views

urlpatterns = [
    path("entrie/list", views.EntriesList.as_view(), name="entrielist"),
    path("entrie/create", views.EntriesCreate.as_view(), name="entriecreate"),
    path("entrie/update/<pk>", views.EntriesUpdate.as_view(), name="entrieupdate"),
    path("entrie/delete/<pk>", views.EntriesDelete.as_view(), name="entriedelete"),
]
