from django.urls import path
from . import views


app_name = 'projects'

urlpatterns = [
    path('home/', views.home, name='home'),
    path("project/<int:pk>/", views.project_detail, name="project_detail"),
    path('add_project/', views.add_project, name='add_project'),
    path("contact/", views.contact, name="contact"),
    path("update_project/<int:pk>/", views.update_project, name="update_project"),
    path("delete_project/<int:pk>/", views.delete_project, name="delete_project"),
    path("services/", views.services, name="services"),
]