from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class Department(models.Model):
    name = models.CharField("Department", max_length=50)


class Form(models.Model):
    """
    Form: Stores the form for the respective criteria
    As each type of user has different forms to be displayed
    """

    title = models.CharField("Form Title", max_length=50)
    description = models.CharField("Form Description", max_length=250)

    department = models.ForeignKey("department", on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', on_delete=None)

    def has_answers(self):
        answers = list()
        for que in self.questions.all():
            if que.answers.all():
                answers.extend(que.answers.all())
        if answers:
            return True
        return False


class Question(models.Model):
    """
    Question: Holds the questions for respective forms
    """

    form = models.ForeignKey(
        "Form", on_delete=models.CASCADE, related_name="questions"
    )
    text = RichTextField("Question")


class Answer(models.Model):
    """
    Answers: stores the answers of the users
    """

    question = models.ForeignKey("question", on_delete=None, related_name='answers')
    text = RichTextUploadingField("Answer")


    def __str__(self):
        return self.question.text