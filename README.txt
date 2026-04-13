# 準備：先引入我們寫好的模型
from polls.models import Question, Choice

# 任務 1：取出第一筆 Question [1]
q = Question.objects.first()
print(q)

# 任務 2：印出第一筆 Question 的所有 Choice [1]
choices = q.choice_set.all()
print(choices)

# 任務 3：把其中一個 Choice.votes 加 1 後儲存 [1]
c = choices.first()
print("原本票數:", c.votes)
c.votes += 1
c.save()
print("加 1 後票數:", c.votes)
print("加 1 後票數:", c.votes)