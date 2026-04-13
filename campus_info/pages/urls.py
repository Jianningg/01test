from django.urls import path
# 確保這裡引入的是 home_page_view
from .views import home_page_view, AboutPageView, clubs_page_view, faq_page_view, SchedulePageView

urlpatterns = [
    path("home/", home_page_view, name="home"), 
    path("clubs/", clubs_page_view, name="clubs"),
    path("schedule/", SchedulePageView.as_view(), name="schedule"),
    path("faq/", faq_page_view, name="faq"),
    path("about/", AboutPageView.as_view(), name="about"),
]