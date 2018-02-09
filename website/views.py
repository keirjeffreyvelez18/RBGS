from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from .models import Program, NewsPost, FacultyMember, OutreachPost
from django.forms import ModelForm
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.list import ListView

class ProgramForm(ModelForm):
    class Meta:
        model = Program
        fields = ['program_name','program_description','program_department']

def list(request):
	program_list = Program.objects.all()
	page = request.GET.get('page', 1)
	paginator = Paginator(program_list, 8)
	try:
		programs = paginator.page(page)
	except PageNotAnInteger:
		programs = paginator.page(1)
	except EmptyPage:
		programs = paginator.page(paginator.num_pages)
	return render(request, 'website/list.html', {'programs': programs})

def outreach(request):
	outreach_list = OutreachPost.objects.all().order_by('-outreach_date')
	page = request.GET.get('page', 1)
	paginator = Paginator(outreach_list, 6)
	try:
		outreach = paginator.page(page)
	except PageNotAnInteger:
		outreach = paginator.page(1)
	except EmptyPage:
		outreach = paginator.page(paginator.num_pages)
	return render(request, 'website/outreach.html', {'outreach': outreach})

def program_item(request, pk, template_name='website/program_item.html'):
	program = get_object_or_404(Program, pk=pk)
	return render(request, template_name, {'object': program})

def news_item(request, pk, template_name='website/news_item.html'):
	news = get_object_or_404(NewsPost, pk=pk)
	return render(request, template_name, {'object': news})

def item_outreach(request, pk, template_name='website/outreach_item.html'):
	outreach = get_object_or_404(OutreachPost, pk=pk)
	return render(request, template_name, {'object': outreach })

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

def index (request):
	template = loader.get_template('website/index.html')
	return HttpResponse (template.render({},request))

def program(request):
	template = loader.get_template('website/program.html')
	return HttpResponse(template.render({}, request))

def research(request):
	template = loader.get_template('website/research.html')
	return HttpResponse(template.render({}, request))

def faculty(request, template_name='website/faculty.html'):
	firstsem = FacultyMember.objects.filter(First_Semester__exact=True)
	secondsem = FacultyMember.objects.filter(Second_Semester__exact=True)
	data = {}
	data['firstsem'] = firstsem
	data['secondsem'] = secondsem
	return render(request, template_name, data )

def news(request, template_name='website/news.html'):
	news = NewsPost.objects.all()
	data = {'news' : news}
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