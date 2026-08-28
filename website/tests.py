import json
import re

from django.test import TestCase


class SeoEndpointTests(TestCase):
    host = "prengaconstruction.al"

    def test_robots_txt(self):
        response = self.client.get("/robots.txt", HTTP_HOST=self.host)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "text/plain")
        self.assertContains(response, "User-agent: *")
        self.assertContains(response, "Disallow: /admin/")
        self.assertContains(
            response,
            "Sitemap: https://prengaconstruction.al/sitemap.xml",
        )

    def test_sitemap_uses_production_domain_and_contains_static_pages(self):
        response = self.client.get("/sitemap.xml", HTTP_HOST=self.host, secure=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "application/xml")
        self.assertContains(response, "https://prengaconstruction.al/")
        self.assertContains(response, "https://prengaconstruction.al/sherbimet/")
        self.assertContains(response, "https://prengaconstruction.al/projektet/")
        self.assertContains(response, "https://prengaconstruction.al/rreth-nesh/")
        self.assertContains(response, "https://prengaconstruction.al/kontakt/")


class ServicesPageSeoTests(TestCase):
    def test_services_page_has_optimized_heading_and_service_sections(self):
        response = self.client.get(
            "/sherbimet/",
            HTTP_HOST="prengaconstruction.al",
            secure=True,
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response,
            '<link rel="canonical" href="https://prengaconstruction.al/sherbimet/">',
            html=True,
        )
        self.assertContains(
            response,
            '<meta property="og:url" content="https://prengaconstruction.al/sherbimet/">',
            html=True,
        )
        self.assertContains(
            response,
            "<h1>Ndërtim dhe riparim çatie në Durrës</h1>",
            html=True,
        )
        for heading in (
            "Ndërtim çatie",
            "Riparim çatie",
            "Rikonstruksion çatie",
            "Punime druri",
        ):
            self.assertContains(response, f"<h2>{heading}</h2>", html=True)


class LocalBusinessStructuredDataTests(TestCase):
    def test_homepage_contains_valid_local_business_data(self):
        response = self.client.get("/")
        html = response.content.decode()
        match = re.search(
            r'<script type="application/ld\+json">\s*(.*?)\s*</script>',
            html,
            re.DOTALL,
        )

        self.assertIsNotNone(match)
        data = json.loads(match.group(1))
        self.assertEqual(data["@type"], "LocalBusiness")
        self.assertEqual(data["url"], "https://prengaconstruction.al/")
        self.assertEqual(data["telephone"], "+355693345460")
        self.assertEqual(data["address"]["addressLocality"], "Durrës")
        self.assertEqual(data["address"]["addressCountry"], "AL")

# Create your tests here.
