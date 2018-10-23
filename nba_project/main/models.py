from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class Department(models.Model):
	name = models.CharField("Department", max_length=50)


class Part1(models.Model):
	department = models.ForeignKey('department', on_delete=models.CASCADE)
	user = models.ForeignKey('users.user', on_delete=models.CASCADE)

	que_1 = RichTextUploadingField(
			"State the Vision and Mission of the Department and Institute"
		)
	que_2 = RichTextUploadingField(
			"State the Program Educational Objectives (PEOs)"
		)
	que_3 = RichTextUploadingField(
			"Indicate where the Vision, Mission and PEOs are published and disseminated among stakeholders"
		)
	que_4 = RichTextUploadingField(
			"State the process for defining the Vision and Mission of the Department, and PEOs of the program"
		)
	que_5 = RichTextUploadingField(
			"Establish consistency of PEOs with Mission of the Department"
		)