from django.db import models
from datetime import time

class Program(models.Model):
	program_name = models.CharField(null="", max_length=100)
	program_description = models.CharField(null="", max_length=2000)
	program_department = models.CharField(null="", max_length=50)
	program_level = models.CharField(null="", max_length=1000)

	def __str__(self):
		return self.program_name

class UpcomingEvent(models.Model):
	event_name = models.CharField(null="",max_length=1000)
	event_details = models.CharField(null="",max_length=10000)
	event_date = models.DateField(null="")
	event_time = models.TimeField(null="", help_text="Format: HH:MM:SS, 24H. e.g 15:30:00 is 3:30PM")
	event_datecreated = models.DateTimeField(null="",auto_now_add=True)

	def __str__(self):
		return self.event_name

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
	news_date = models.DateField(null="")
	news_time = models.TimeField(null="", auto_now_add=True)

	def __str__(self):
		return  self.news_title

class Alumni(models.Model):
	alumni_name = models.CharField(null="", max_length=1000, help_text="Full name along with prefix and suffixes.")
	alumni_description = models.CharField(null="", max_length=5000, help_text="Short Bio of the alumni")
	alumni_contact = models.CharField(null="", max_length=5000, help_text="LinkedIn URL, Contact Number")
	alumni_image = models.FileField(null="", help_text="2x2 or Professional Image of the Alumni")
	alumni_url = models.URLField(null="", help_text="LinkedIn / Professional Website of the Alumni")

	def __str__(self):
		return self.alumni_name


# to migrate database use the following commands
# python manage.py makemigrations [nameofApp]
# python manage.py sqlmigrate [nameofApp] ###
# python manage.py migrate
