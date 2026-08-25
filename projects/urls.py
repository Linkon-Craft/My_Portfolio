from django.urls import path
from . import views


app_name = 'projects'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('projects/', views.project_list, name='project_list'), 
    path("project/<int:pk>/", views.project_detail, name="project_detail"),
    path('add_project/', views.add_project, name='add_project'),
    path("contact/", views.contact, name="contact"),
]