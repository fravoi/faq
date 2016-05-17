from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader

from .models import Theme, Questionreponse

def index(request ):
    latest_theme_list = Theme.objects.order_by('-pub_date_theme')[:]
    context = {
        'latest_theme_list': latest_theme_list,
    }
    return render(request,'appfaq/detail.html', context)
    
def detail(request, theme_id):
    t=Theme.objects.get(pk=theme_id)
    return t.theme_text
	#return render(request, 'appfaq/detail.html', {'thème': t})

def results(request, questionreponse_id):
    return HttpResponse("Vous regardez actuellement la question-réponse %s." % questionreponse_id)