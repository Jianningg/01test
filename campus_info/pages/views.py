from django.shortcuts import render
from django.views.generic import TemplateView

# 確保函式名稱是 home_page_view，不是 home
def home_page_view(request):
    return render(request, "home.html", {"title": "Campus Activity Info Station"})
# 2. 關於本站 (Class-based view)
class AboutPageView(TemplateView):
    template_name = "about.html"

# 3. 社團列表
def clubs_page_view(request):
    clubs_data = [
        {"name": "robotics club", "advisor": "Prof. Chen", "officers": ["Alicia", "Kevin"], "activities": ["Arduino workshop"]},
        {"name": "music club", "advisor": "Prof. Lin", "officers": ["Leo", "Sophie"], "activities": ["Choir rehearsal"]},
        {"name": "photography club", "advisor": "Prof. Wang", "officers": ["Brian", "Nina"], "activities": ["Night walk"]},
        {"name": "volunteer club", "advisor": "Prof. Hsu", "officers": ["Amy"], "activities": ["Beach cleanup"]}
    ]
    return render(request, "clubs.html", {"clubs_data": clubs_data})

# 4. 一週行程 (覆寫 get_context_data，提供3層巢狀資料)
class SchedulePageView(TemplateView):
    template_name = "schedule.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 巢狀結構：每天 -> 每時段 -> 多個活動
        context["schedule"] = [
            {"day": "Monday", "slots": [
                {"time": "Morning", "events": ["Orientation", "Coding warm-up"]},
                {"time": "Noon", "events": ["Career talk"]},
                {"time": "Afternoon", "events": ["Basketball trial"]}
            ]},
            {"day": "Tuesday", "slots": [
                {"time": "Morning", "events": ["English corner"]},
                {"time": "Afternoon", "events": ["Photography walk"]}
            ]},
            {"day": "Wednesday", "slots": []}, # 刻意留空測試
            {"day": "Thursday", "slots": [{"time": "Morning", "events": ["Volunteer briefing"]}]},
            {"day": "Friday", "slots": [{"time": "Afternoon", "events": ["Sports day planning"]}]}
        ]
        return context

# 5. FAQ 常見問題
def faq_page_view(request):
    faq_data = [
        {"category": "Registration", "questions": ["How do I register?", "Can I join two clubs?"]},
        {"category": "New Students", "questions": []} # 刻意留空以觸發 {% empty %}
    ]
    return render(request, "faq.html", {"faq_data": faq_data})
