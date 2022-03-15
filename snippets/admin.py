from atexit import register
from django.contrib import admin
from snippets.models import Snippet

@admin.register(Snippet)
class SnippetAdmin(admin.ModelAdmin):
    pass
