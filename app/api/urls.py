from django.urls import path
from . import views

urlpatterns = [
        path("wines", views.wines),
        path("notes", views.notes),
        path("value", views.value),
]
