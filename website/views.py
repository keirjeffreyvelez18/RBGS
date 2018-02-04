from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from .models import Program, NewsPost
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

def education(request, template_name='website/list_filtered.html'):
	programs = Program.objects.filter(program_department__exact="Education")
	data = {}
	data['object_list'] = programs
	data['dept'] = "Education"
	return render(request, template_name, data )

def business(request, template_name='website/list_filtered.html'):
	programs = Program.objects.filter(program_department__exact="Business Management and Administration")
	data = {}
	data['object_list'] = programs
	data['dept'] = "Business Management and Administration"
	return render(request, template_name, data )

def administration(request, template_name='website/list_filtered.html'):
	programs = Program.objects.filter(program_department__exact="Public Administration and Governance")
	data = {}
	data['object_list'] = programs
	data['dept'] = "Public Administration and Governance"
	return render(request, template_name, data )

def management(request, template_name='website/list_filtered.html'):
	programs = Program.objects.filter(program_department__exact="Development Management")
	data = {}
	data['object_list'] = programs
	data['dept'] = "Development Management"
	return render(request, template_name, data )

def computer_studies(request, template_name='website/list_filtered.html'):
	programs = Program.objects.filter(program_department__exact="Computer Studies")
	data = {}
	data['object_list'] = programs
	data['dept'] = "Computer Studies"
	return render(request, template_name, data )

def criminal_justice(request, template_name='website/list_filtered.html'):
	programs = Program.objects.filter(program_department__exact="Criminal Justice Education")
	data = {}
	data['object_list'] = programs
	data['dept'] = "Criminal Justice Education"
	return render(request, template_name, data )

def psychology(request, template_name='website/list_filtered.html'):
	programs = Program.objects.filter(program_department__exact="Psychology and Guidance and Counseling")
	data = {}
	data['object_list'] = programs
	data['dept'] = "Psychology and Guidance and Counseling"
	return render(request, template_name, data )

def nursing(request, template_name='website/list_filtered.html'):
	programs = Program.objects.filter(program_department__exact="Nursing")
	data = {}
	data['object_list'] = programs
	data['dept'] = "Nursing"
	return render(request, template_name, data )

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

def news(request, template_name='website/news.html'):
	news = NewsPost.objects.all()
	data = {}
	data['object_list'] = news
	return render(request, template_name, data)

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