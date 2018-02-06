from django.contrib import admin
from . models import Program, BlogPost, NewsPost, FacultyMember

admin.site.register(Program)
admin.site.register(BlogPost)
admin.site.register(NewsPost)
admin.site.register(FacultyMember)

