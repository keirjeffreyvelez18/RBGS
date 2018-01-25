from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect

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

def programlist(request):
	template = loader.get_template('website/programlist.html')
	return HttpResponse(template.render({}, request))