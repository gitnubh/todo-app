from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('done/<int:taskid>/',views.done,name='done'),
    path('edit/<int:form_id>/',views.edit,name='edit'),
    path('tasklv/',views.Tasklv.as_view(),name = 'tasklv'),
    path('taskdv/<int:pk>',views.Taskdv.as_view(),name = 'taskdv'),
    path('taskuv/<int:pk>',views.Taskuv.as_view(),name = 'taskuv'),
    path('taskdelv/<int:pk>',views.TaskDelV.as_view(),name = 'taskdelv')
]