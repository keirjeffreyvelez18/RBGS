from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from django.forms import ModelForm
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.list import ListView
import time
import calendar


from .models import Program, NewsPost, FacultyMember, OutreachPost, UpcomingEvent, Alumni

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

def news(request, template_name='website/news.html'):
	news_list = NewsPost.objects.all().order_by('-news_date','-news_time')
	page = request.GET.get('page', 1)
	paginator = Paginator(news_list, 3)
	months = mkmonth_lst()

	try:
		news = paginator.page(page)
	except PageNotAnInteger:
		news = paginator.page(1)
	except EmptyPage:
		news = paginator.page(paginator.num_pages)
	return render(request, template_name, {'news' : news,"months":months})

def upcomingevents(request, template_name='website/upcomingevents.html'):
	events_list = UpcomingEvent.objects.all().order_by('event_date')
	page = request.GET.get('page', 1)
	paginator = Paginator(events_list, 3)

	try:
		events = paginator.page(page)
	except PageNotAnInteger:
		events = paginator.page(1)
	except EmptyPage:
		events = paginator.page(paginator.num_pages)
	return render(request, template_name, {'events' : events})

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

def alumni(request):
	alumni_list = Alumni.objects.all().order_by('-outreach_date')
	page = request.GET.get('page', 1)
	paginator = Paginator(alumni_list, 6)
	try:
		alumni = paginator.page(page)
	except PageNotAnInteger:
		alumni = paginator.page(1)
	except EmptyPage:
		alumni = paginator.page(paginator.num_pages)
	return render(request, 'website/alumni.html', {'alumni': alumni})

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

def index (request, template_name='website/index.html'):
	news = NewsPost.objects.order_by('-news_date','-news_time')[0]
	events = UpcomingEvent.objects.order_by('event_date','event_time')[0]
	outreach = OutreachPost.objects.order_by('-outreach_date')[0]
	return render(request, template_name, {'news':news,'events':events,'outreach':outreach})

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

def contactus(request):
	template = loader.get_template('website/contactus.html')
	return HttpResponse(template.render({}, request))

def mkmonth_lst():
	if not NewsPost.objects.count(): return []

	# set up vars
	year, month = time.localtime()[:2]
	first = NewsPost.objects.order_by("news_date")[0]
	fyear = first.news_date.year
	fmonth = first.news_date.month
	months = []

	# loop over years and months
	for y in range(year, fyear-1, -1):
		start, end = 12, 0
		if y == year: start = month
		if y == fyear: end = fmonth-1

		for m in range(start, end, -1):
			months.append((y, m, calendar.month_name[m]))
	return months





def login(request, template_name='website/login.html'):
	return render(request, template_name)

def dashboard(request, template_name='website/dashboard.html'):
	events_list = UpcomingEvent.objects.all().order_by('event_date')
	events_count = events_list.count()
	news_list = NewsPost.objects.all().order_by('-news_date','-news_time')
	latest_news = news_list[0]
	news_count = news_list.count()
	outreach_list = OutreachPost.objects.all().order_by('-outreach_date')
	outreach_count = outreach_list.count()
	context = {'events_list':events_list, 'events_count':events_count,
			   'news_list':news_list,'news_count':news_count,
			   'latest_news':latest_news,'outreach_list':outreach_list,
			   'outreach_count':outreach_count
			   }
	return render(request, template_name, context)

def postlist(request, string, template_name='website/post-list.html'):
	context = {}
	if string=='News':
		context = NewsPost.objects.all().order_by('-news_date','-news_time')
	if string=='Events':
		context = UpcomingEvent.objects.all().order_by('event_date')

	page = request.GET.get('page', 1)
	paginator = Paginator(context, 10)

	try:
		content = paginator.page(page)
	except PageNotAnInteger:
		content = paginator.page(1)
	except EmptyPage:
		content = paginator.page(paginator.num_pages)
	return render(request, template_name, {'content':content,'post':string})