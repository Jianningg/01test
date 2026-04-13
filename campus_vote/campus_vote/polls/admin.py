from django.contrib import admin
from .models import Question, Choice

# 將模型註冊到後台
admin.site.register(Question)
admin.site.register(Choice)