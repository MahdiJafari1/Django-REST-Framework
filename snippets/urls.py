from django.urls import path
from snippets import views

urlpatterns = [
    path("snippets/", views.snippet_list, name="snippet_list"),
    path("snippets/<int:pk>", views.snippet_detail, name="snippet")
]
