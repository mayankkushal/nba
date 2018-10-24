from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class Department(models.Model):
	name = models.CharField("Department", max_length=50)


class Part1(models.Model):
	"""
	Criterion 1: Vision, Mission and Program Educational Objectives (60)
	"""

	department = models.ForeignKey('department', on_delete=models.CASCADE)
	user = models.ForeignKey('users.user', on_delete=models.CASCADE)

	que_1 = RichTextUploadingField(
			"1.1 State the Vision and Mission of the Department and Institute" # Marks: 5
		)
	que_2 = RichTextUploadingField(
			"1.2 State the Program Educational Objectives (PEOs)" # Marks: 5
		)
	que_3 = RichTextUploadingField(
			"1.3 Indicate where the Vision, Mission and PEOs are published and disseminated among stakeholders" # Marks: 10
		)
	que_4 = RichTextUploadingField(
			"1.4 State the process for defining the Vision and Mission of the Department, and PEOs of the program" # Marks: 25
		)
	que_5 = RichTextUploadingField(
			"1.5 Establish consistency of PEOs with Mission of the Department" # Marks: 15
		)

class Part2(models.Model):
	"""
	Criterion 2: Program Curriculum and Teaching–Learning Processes (120)
	"""

	department = models.ForeignKey('department', on_delete=models.CASCADE)
	user = models.ForeignKey('users.user', on_delete=models.CASCADE)

	# 2.1. Program Curriculum (20)
	que_1 = RichTextUploadingField(
			"2.1.1 State the process used to identify extent of compliance of the University curriculum for attaining the Program Outcomes(POs) & Program Specific Outcomes(PSOs), mention the identified curricular gaps, if any" # Marks: 10
		)
	que_2 = RichTextUploadingField(
			"2.1.2 State the delivery details of the content beyond the syllabus for the attainment of POs & PSOs" # Marks: 10
		)

	# 2.2. Teaching-Learning Processes (100)
	que_3 = RichTextUploadingField(
			"2.2.1 Describe the Process followed to improve quality of Teaching Learning" # Marks: 25
		)
	que_4 = RichTextUploadingField(
			"2.2.2 Quality of internal semester Question papers, Assignments and Evaluation" # Marks: 20
		)
	que_5 = RichTextUploadingField(
			"2.2.3 Quality of student projects" # Marks: 25
		)
	que_6 = RichTextUploadingField(
			"2.2.4 Initiatives related to industry interaction" # Marks: 15
		)
	que_7 = RichTextUploadingField(
			"2.2.5 Initiatives related to industry internship/summer training" # Marks: 15
		)

class Part3(models.Model):
	"""
	Criterion 3: Course Outcomes and Program Outcomes (120)
	"""
	
	department = models.ForeignKey('department', on_delete=models.CASCADE)
	user = models.ForeignKey('users.user', on_delete=models.CASCADE)

	# 3.1 Establish the correlation between the courses and the POs & PSOs (20)
	que_1 = RichTextUploadingField(
			"3.1.1 Course Outcomes" # Marks: 5
		)
	que_2 = RichTextUploadingField(
			"3.1.2 CO-PO/PSOs matrices of courses selected in 3.1.1 (six matrices)" # Marks: 5
		)
	que_3 = RichTextUploadingField(
			"3.1.3 Program level Course-PO/PSOs matrix of ALL courses including first year courses" # Marks: 10
		)

	# 3.2 Attainment of Course Outcomes (50)
	que_4 = RichTextUploadingField(
			"3.2.1 Describe the assessment processes used to gather the data upon which the evaluation of Course Outcome is based" # Marks: 10
		)
	que_5 = RichTextUploadingField(
			"3.2.2 Record the attainment of Course Outcomes of all courses with respect to set attainment levels" # Marks: 40
		)

	# 3.3 Attainment of Program Outcomes and Program Specific Outcomes (50)
	que_6 = RichTextUploadingField(
			"3.3.1. Describe assessment tools and processes used for assessing the attainment of each of the POs & PSOs" # Marks: 10
		)
	que_7 = RichTextUploadingField(
			"3.3.2 Provide results of evaluation of each PO & PSO" # Marks: 40