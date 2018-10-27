from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
	user=models.OneToOneField(
		User,
		on_delete=models.CASCADE,
		primary_key=True,
	)
	choices= (
		("TEACHER", 'teacher'),
		("ADMIN", 'admin'),
		("PRINCIPAL", 'principal'),
	)
	profession = models.CharField(max_length=9,
		choices=choices,
		default="TEACHER",
	)

	def __str__(self):
		return str(self.user)

class Classroom(models.Model):
	standard=models.CharField(max_length=50, blank=True)
	section=models.CharField(max_length=10, blank=True)
	classteacher=models.ForeignKey(Profile, on_delete=models.CASCADE)
	numstudents=models.IntegerField(null=True)

	def __str__(self):
		return f"{self.standard} {self.section}"


class Student(models.Model):
	name=models.CharField(max_length=50, blank=True)
	rollnumber = models.IntegerField(null=True)
	parentname=models.CharField(max_length=50, blank=True)
	parentnum=models.IntegerField(null=True)
	dob=models.DateField(max_length=8)
	classroom=models.ForeignKey(Classroom, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.name

class Subject(models.Model):
	subjectname= models.CharField(max_length=50, blank=True)

	def __str__(self):
		return self.subjectname


class Exam(models.Model):
	examname= models.CharField(max_length=50, blank=True)
	classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)


	def __str__(self):
		return f"{self.examname} {self.classroom}"

class Test(models.Model):
	subject=models.ForeignKey(Subject, on_delete=models.CASCADE)
	maxmarks=models.IntegerField(null=True)
	duration=models.IntegerField(null=True)
	evaluatedby=models.ForeignKey(Profile, on_delete=models.CASCADE)
	exam=models.ForeignKey(Exam,on_delete=models.CASCADE, null=True)
	classroom=models.ForeignKey(Classroom, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return f"{self.subject} {self.classroom}"

class Score(models.Model):
	exam=models.ForeignKey(Exam, on_delete=models.CASCADE)
	test=models.ForeignKey(Test, on_delete=models.CASCADE)
	student=models.ForeignKey(Student, on_delete=models.CASCADE)
	score=models.FloatField(default=0.0)
	classroom=models.ForeignKey(Classroom, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return f"{self.test} {self.student} {self.score}"



	


