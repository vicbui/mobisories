from django.template import RequestContext
from django.shortcuts import render,render_to_response
from django.http import HttpResponse

def index(request):
	context = RequestContext(request)
	context_dict = {'bold_message': "I am starting the evolution"}
	return render_to_response('mobisories/index.html', context_dict, context)