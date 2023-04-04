from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, DeleteView, TaskReorder
from django.contrib.auth.views import LogoutView #we dont need a seperate view fun only build in

urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'), #pk is primaty key
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'), #pk is primaty key
    path('task-delete/<int:pk>/', DeleteView.as_view(), name='task-delete'), #pk is primaty key
    path('task-reorder/', TaskReorder.as_view(), name='task-reorder'),

]
