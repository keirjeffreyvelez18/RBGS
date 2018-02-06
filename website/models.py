from django.db import models


class Program (models.Model):
	program_name = models.CharField(null="", max_length=100)
	program_description = models.CharField(null="", max_length=2000)
	program_department = models.CharField(null="", max_length=50)

	def __str__(self):
		return self.program_name


class BlogPost(models.Model):
	blog_title = models.CharField(null="", max_length=50)
	blog_author = models.CharField(null="", max_length=50)
	blog_date = models.DateField()
	blog_content = models.CharField(null="", max_length=5000)
	blog_image = models.FileField()

class FacultyMember(models.Model):
	faculty_Last_Name = models.CharField(null="", max_length=100)
	faculty_First_Name = models.CharField(null="", max_length=100)
	faculty_Middle_Name = models.CharField(null="", max_length=100)
	First_Semester = models.BooleanField(default=True)
	Second_Semester = models.BooleanField(default=True)

	def __str__(self):
		return self.faculty_Last_Name+", "+self.faculty_First_Name

class OutreachPost(models.Model):
	outreach_title = models.CharField(null="", max_length=50)
	outreach_author = models.CharField(null="", max_length=50)
	outreach_date = models.DateField()
	outreach_content = models.CharField(null="", max_length=5000)
	outreach_image = models.FileField()

class NewsPost(models.Model):
	news_title = models.CharField(null="", max_length=1000)
	news_description = models.CharField(null="",max_length=10000)
	news_author = models.CharField(null="",max_length=1000)
	news_image = models.FileField(null=" ")

	def __str__(self):
		return self.news_title


# to migrate database use the following commands
# python manage.py makemigrations [nameofApp]
# python manage.py sqlmigrate [nameofApp] ###
# python manage.py migrate
