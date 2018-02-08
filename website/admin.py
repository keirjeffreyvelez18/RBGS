from django.contrib import admin
from . models import Program, BlogPost, NewsPost, FacultyMember, ResearchTitle

admin.site.register(Program)
admin.site.register(BlogPost)
admin.site.register(NewsPost)
admin.site.register(FacultyMember)
admin.site.register(ResearchTitle)

