from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    path("snippets/", views.SnippetList.as_view(), name="snippet_list"),
    path("snippets/<int:pk>", views.SnippetDetail.as_view(), name="snippet"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
