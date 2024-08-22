from django.contrib import admin  # noqa
from django_summernote.admin import SummernoteModelAdmin

from .models import Comment, Post


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ("title", "slug", "status")
    search_fields = ["title"]
    list_filter = ("status",)
    prepopulated_fields = {"slug": ("title",)}
    summernote_fields = ("content",)


# Register your models here.

admin.site.register(Comment)
