from django.db import models


class Program (models.Model):
	program_name = models.CharField(null="", max_length=100)
	program_description = models.CharField(null="", max_length=2000)
	program_department = models.CharField(null="", max_length=50)

	def __str__(self):
		return self.program_name

class UpdatePost(models.Model):
	update_title = models.CharField(null="", max_length=1000)

	def __str__(self):
		return self.update_title

class ResearchTitle(models.Model):
	research_title = models.CharField(null="", max_length=1000)
	research_description = models.CharField(null="", max_length=10000)
	research_abstract = models.CharField(null="", max_length=10000)
	research_author = models.CharField(null="", max_length=1000)
	research_resources = models.CharField(null="", max_length=10000)

	def __str__(self):
		return self.research_title+" by "+self.research_author

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
	outreach_date = models.DateField(null="", auto_now_add=True)
	outreach_content = models.CharField(null="", max_length=5000)
	outreach_image = models.FileField()

	class Meta:
		get_latest_by = 'outreach_date'

	def __str__(self):
		return self.outreach_title+" by "+self.outreach_author

class NewsPost(models.Model):
	news_title = models.CharField(null="", max_length=1000, help_text="Headline")
	news_shortdesc = models.CharField(null="", max_length=10000, help_text="Short Description for Preview text.")
	news_description = models.CharField(null="",max_length=10000, help_text="Full content")
	news_author = models.CharField(null="",max_length=1000, help_text="Author of the article")
	news_image = models.FileField(null="", help_text="Headline Image of the article")
	news_date = models.DateField(null="", auto_now_add=True)
	news_time = models.TimeField(null="", auto_now_add=True)

	def __str__(self):
		return  self.news_title


# to migrate database use the following commands
# python manage.py makemigrations [nameofApp]
# python manage.py sqlmigrate [nameofApp] ###
# python manage.py migrate
