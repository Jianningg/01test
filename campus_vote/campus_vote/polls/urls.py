from django.urls import path
# 請注意：這三個名稱必須跟 views.py 裡面定義的一模一樣
from .views import QuestionListView, question_detail_view, stats_view

urlpatterns = [
    path("", QuestionListView.as_view(), name="home"),
    path("question/<int:pk>/", question_detail_view, name="question_detail"),
    path("stats/", stats_view, name="stats"),
]