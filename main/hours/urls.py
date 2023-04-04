from django.urls import path

from django.contrib.auth.views import LogoutView #we dont need a seperate view fun only build in
from . import views

urlpatterns = [
    path("inputhour/list", views.HoursList.as_view(), name="inputhourlist"),
    path("inputhour/create", views.HoursListCreate.as_view(), name="inputhourcreate"),
    path("inputhour/update/<pk>", views.HoursListUpdate.as_view(), name="inputhourupdate"),
    path("inputhour/delete/<pk>", views.HoursListDelete.as_view(), name="inputhourdelete"),
]