from django.contrib import admin
from .models import Project, Review
from . import models
# Register your models here.


admin.site.register(models.Project)
admin.site.register(models.Review)

# @admin.register(Project)
# @admin.register(Review)


class ReviewAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "project",
        "rating",
        "approved",
        "created_at",
    )

    list_filter = (
        "approved",
        "rating",
        "created_at",
    )

    search_fields = (
        "name",
        "comment",
        "project__title",
    )

    list_editable = (
        "approved",
    )