from django.db import models


class Program (models.Model):
	program_name = models.CharField(null="", max_length=50)
	program_description = models.CharField(null="", max_length=1000)
	program_department = models.CharField(null="", max_length=50)


class BlogPost(models.Model):
	blog_title = models.CharField(null="", max_length=50)
	blog_author = models.CharField(null="", max_length=50)
	blog_date = models.DateField()
	blog_content = models.CharField(null="", max_length=5000)
	blog_image = models.FileField()




# to migrate database use the following commands
# python manage.py makemigrations [nameofApp]
# python manage.py sqlmigrate [nameofApp] ###
# python manage.py migrate
