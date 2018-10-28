from django.shortcuts import render
from django.views.generic import FormView
from django.forms.models import modelformset_factory
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from .forms import AnswerForm
from .models import Answer, Question, Form

# Create your views here.

class MainView(FormView):
    template_name = "main/index.html"
    form_class = AnswerForm

    def get(self, *args, **kwargs):
        user = self.request.user

        form = Form.objects.get(user=user, department=user.department)
        if form.has_answers():
            return HttpResponseRedirect(reverse_lazy("main:update"))
        super(MainView, self).get(**kwargs) 

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        user = self.request.user

        form = Form.objects.get(user=user, department=user.department)
        context['form'] = form

        questions = form.questions.all()
        question_count = questions.count()

        AnswerFormset = modelformset_factory(
            Answer,
            form=self.form_class,
            extra=question_count,
        )

        formset = AnswerFormset(
            queryset=Answer.objects.none()
        )
        context["formset"] = formset
        context["formset_zip"] = zip(formset, questions)

        return context

    def post(self, request, *args, **kwargs):
        AnswerFormset = modelformset_factory(Answer, form=AnswerForm)
        formset = AnswerFormset(request.POST)


        form = Form.objects.get(user=self.request.user, department=self.request.user.department)
        questions = form.questions.all()

        if formset.is_valid():
            for f, que in zip(formset, questions):
                text = f.cleaned_data.get('text')
                if text:
                    Answer.objects.create(
                            question=que,
                            text=text
                        )
        return HttpResponseRedirect(reverse_lazy("main:update"))


class MainUpdateView(FormView):
    template_name = "main/index.html"
    form_class = AnswerForm

    def get_context_data(self, **kwargs):
        context = super(MainUpdateView, self).get_context_data(**kwargs)
        user = self.request.user
        form = Form.objects.get(user=user, department=user.department)
        context['form'] = form
        questions = form.questions.all()
        

        if form.has_answers():
            question_count = questions.count()

            AnswerFormset = modelformset_factory(
                Answer,
                form=self.form_class,
                extra=question_count,
            )
            formset = AnswerFormset()
            context["formset"] = formset
            context["formset_zip"] = zip(formset, questions)

        return context

    def post(self, request, *args, **kwargs):
        AnswerFormset = modelformset_factory(Answer, form=AnswerForm)
        formset = AnswerFormset(request.POST)


        form = Form.objects.get(user=self.request.user, department=self.request.user.department)
        questions = form.questions.all()

        if formset.is_valid():
            for f, que in zip(formset, questions):
                text = f.cleaned_data.get('text')
                print(text, que)
                if text:
                    ans = Answer.objects.get(question=que)
                    ans.text = text
                    ans.save()
        return HttpResponseRedirect(reverse_lazy("main:update"))