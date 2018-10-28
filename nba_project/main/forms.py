from django import forms
from django.forms.models import modelformset_factory

from .models import Answer, Question


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ("text",)

AnswerFormSet = modelformset_factory(Answer, form=AnswerForm)
