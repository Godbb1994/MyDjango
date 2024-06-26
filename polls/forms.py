from django import forms
from .models import Question, Choice

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["question_text", "pub_date", "type"]

class QuestionFormMultipleChoices(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["question_text", "pub_date", "type"]
        widgets = {
            "type": forms.RadioSelect(),
        }
