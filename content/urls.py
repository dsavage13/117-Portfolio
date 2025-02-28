from django.urls import path
from content import views

urlpatterns = [
    path('', views.project_list_view, name='project_list'),
    path('add/', views.add_project_view, name='add'),
]
