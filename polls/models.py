# models.py start
from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=10, choices=[('single', 'Single Choice'), ('multiple', 'Multiple Choice')])

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - timezone.timedelta(days=1) <= self.pub_date <= now

    # 新增順序欄位
    position = models.IntegerField(default=0, null=True)




class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

# models.py end
