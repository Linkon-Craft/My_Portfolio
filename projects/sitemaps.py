from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .models import Project


class StaticViewSitemap(Sitemap):

    priority = 0.8
    changefreq = "monthly"

    def items(self):
        return [
            "home",
            "services"
        ]

    def location(self, item):
        return reverse(
            f"projects:{item}"
        )


class ProjectSitemap(Sitemap):

    priority = 0.7
    changefreq = "monthly"

    def items(self):
        return Project.objects.all()

    def location(self, obj):
        return reverse(
            "projects:project_detail",
            kwargs={"pk": obj.pk}
        )