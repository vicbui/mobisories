from django.template import RequestContext
from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from mobisories.models import * 

def index(request):
	context = RequestContext(request)
	entities = Entity.objects.all()
	context_dict = {'entities':entities,'bold_message': "I am starting the evolution"}
	return render_to_response('mobisories/index.html', context_dict, context)	