from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from .models import Question, Choice

class CampusVoteTests(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        # 建立測試資料庫，這個方法只會執行一次，速度較快
        cls.question = Question.objects.create(
            title="是否需要增設飲水機？",
            pub_date=timezone.now(),
            description="測試描述內容",
            is_open=True
        )
        cls.choice = Choice.objects.create(
            question=cls.question,
            choice_text="非常需要",
            votes=10
        )

    # 1. model 欄位內容測試 (Question)
    def test_question_model_content(self):
        self.assertEqual(self.question.title, "是否需要增設飲水機？")
        self.assertTrue(self.question.is_open)

    # 2. model 欄位內容測試 (Choice)
    def test_choice_model_content(self):
        self.assertEqual(self.choice.choice_text, "非常需要")
        self.assertEqual(self.choice.votes, 10)

    # 3. __str__() 測試
    def test_model_str(self):
        self.assertEqual(str(self.question), "是否需要增設飲水機？")
        self.assertEqual(str(self.choice), "非常需要")

    # 4. ForeignKey 關聯正確性測試
    def test_foreign_key_relation(self):
        # 測試選項是否真的關聯到該問題
        self.assertEqual(self.choice.question, self.question)

    # 5. URL by path 測試 (首頁 /)
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    # 6. URL by name (reverse) 測試
    def test_url_available_by_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    # 7. template name 測試
    def test_template_name_correct(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html")
        self.assertTemplateUsed(response, "base.html")

    # 8. template content 測試
    def test_template_content(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "所有投票題目")

    # 9. 首頁能正確顯示資料庫建立的測試資料
    def test_homepage_displays_test_data(self):
        response = self.client.get(reverse("home"))
        # 檢查問題標題與選項有沒有被正確渲染出來
        self.assertContains(response, "是否需要增設飲水機？")
        self.assertContains(response, "非常需要")

    # 10. 詳細頁與統計頁的 URL 與狀態碼測試 (湊滿10個測試)
    def test_other_pages_work(self):
        # 測試單一問題詳細頁
        detail_url = reverse("question_detail", kwargs={"pk": self.question.pk})
        detail_response = self.client.get(detail_url)
        self.assertEqual(detail_response.status_code, 200)
        
        # 測試統計頁
        stats_response = self.client.get(reverse("stats"))
        self.assertEqual(stats_response.status_code, 200)