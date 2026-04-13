from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Question, Choice

# 1. 首頁：使用 ListView 顯示所有 Question
class QuestionListView(ListView):
    model = Question
    template_name = "home.html"
    context_object_name = "question_list" # ListView 預設會將資料裝在這個變數中

# 2. 單一問題詳細頁：使用 function-based view
def question_detail_view(request, pk):
    # 透過 pk 抓取對應的問題，找不到則回傳 404
    question = get_object_or_404(Question, pk=pk)
    return render(request, "question_detail.html", {"question": question})

# 3. 統計頁面：顯示各項數據
def stats_view(request):
    total_questions = Question.objects.count()
    total_choices = Choice.objects.count()
    open_questions = Question.objects.filter(is_open=True).count()
    
    # 計算每題最高票選項
    highest_votes = []
    for q in Question.objects.all():
        # 依照 votes 欄位由大到小排序，取第一筆
        top_choice = q.choice_set.order_by('-votes').first() 
        highest_votes.append({
            'question': q,
            'top_choice': top_choice
        })

    context = {
        "total_questions": total_questions,
        "total_choices": total_choices,
        "open_questions": open_questions,
        "highest_votes": highest_votes,
    }
    return render(request, "stats.html", context)
