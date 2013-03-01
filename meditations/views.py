# Create your views here.

from django.http import HttpResponse
from meditations.models import BookSection
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404

def index(request):
    meditation = BookSection.objects.order_by('?')[0]
    template = loader.get_template('index.html')
    context = RequestContext(request, {
        'meditation': meditation,
    })
    return HttpResponse(template.render(context))

def id(request, meditation_id):
    meditation = get_object_or_404(BookSection, pk=meditation_id)
    template = loader.get_template('index.html')
    context = RequestContext(request, {
        'meditation': meditation,
    })
    return HttpResponse(template.render(context))
    
