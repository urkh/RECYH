# Create your views here.
#from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.db.models import Count



def inicio(request):
    
    return render_to_response('admin.html')

