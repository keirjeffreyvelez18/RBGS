from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from .models import Program
from django.forms import ModelForm
from django.shortcuts import render, redirect, get_object_or_404

class ProgramForm(ModelForm):
    class Meta:
        model = Program
        fields = ['program_name','program_description','program_department']

def list(request, template_name='website/list.html'):
	programs = Program.objects.all()
	data = {}
	data['object_list'] = programs
	return render(request, template_name, data)

# def list_filter(request, department, template_name='website/list_template.html'):
# 	programs = Program.objects.get(program_department=department)
# 	data = {}
# 	data['object_list'] = programs
# 	return render(request, template_name, data)

def program_item(request, pk, template_name='website/program_item.html'):
	program = get_object_or_404(Program, pk=pk)
	return render(request, template_name, {'object':program})

def index (request):
	template = loader.get_template('website/index.html')
	return HttpResponse (template.render({},request))

def program(request):
	template = loader.get_template('website/program.html')
	return HttpResponse(template.render({}, request))

def research(request):
	template = loader.get_template('website/research.html')
	return HttpResponse(template.render({}, request))

def outreach(request):
	template = loader.get_template('website/outreach.html')
	return HttpResponse(template.render({}, request))

def news(request):
	template = loader.get_template('website/news.html')
	return HttpResponse(template.render({}, request))

def contactus(request):
	template = loader.get_template('website/contactus.html')
	return HttpResponse(template.render({}, request))

def content_news(request):
	template = loader.get_template('website/content_news.html')
	return HttpResponse(template.render({}, request))

def content_outreach(request):
	template = loader.get_template('website/content_outreach.html')
	return HttpResponse(template.render({}, request))

def content_programs(request):
	template = loader.get_template('website/content_programs.html')
	return HttpResponse(template.render({}, request))