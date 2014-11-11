from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.
def indice(request):
	return render_to_response("index.html", RequestContext(request))