from django.test import SimpleTestCase
from django.urls import reverse

class CampusPagesTests(SimpleTestCase):
    
    # 1. 測試 URL status code
    def test_url_status_code(self):
        response = self.client.get("/home/")
        self.assertEqual(response.status_code, 200)

    # 2. 測試 reverse() by name
    def test_url_by_name(self):
        response = self.client.get(reverse("clubs"))
        self.assertEqual(response.status_code, 200)

    # 3. 測試 assertTemplateUsed
    def test_template_used(self):
        response = self.client.get(reverse("schedule"))
        self.assertTemplateUsed(response, "schedule.html")
        self.assertTemplateUsed(response, "base.html") # 驗證是否有繼承 base

    # 4. 測試 assertContains
    def test_template_content(self):
        response = self.client.get(reverse("faq"))
        self.assertContains(response, "FAQ")