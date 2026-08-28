from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .models import Project


class StaticViewSitemap(Sitemap):
    protocol = "https"
    priority = 0.8
    changefreq = "monthly"

    def items(self):
        return ["home", "services", "projects", "about", "contact"]

    def location(self, item):
        return reverse(item)


class ProjectSitemap(Sitemap):
    protocol = "https"
    priority = 0.7
    changefreq = "monthly"

    def items(self):
        return Project.objects.all()

    def location(self, project):
        return reverse("project_detail", kwargs={"pk": project.pk})

    def lastmod(self, project):
        return project.created_at
