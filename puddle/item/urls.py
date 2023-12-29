from django.urls import path

from . import views

app_name = "item"

urlpatterns = [
    path("<int:pk>", views.detail, name="detail"),
    path("<int:pk>/delete/", views.delete, name="delete"),
    path("<int:pk>/delete/", views.edit, name="edit"),
]
