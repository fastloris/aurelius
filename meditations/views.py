# Create your views here.

from django.http import HttpResponse
from meditations.models import BookSection
from django.template import Context, loader

def index(request):
    meditation = BookSection.objects.order_by('?')[0]
    template = loader.get_template('index.html')
    context = Context({
        'meditation': meditation,
    })
    return HttpResponse(template.render(context))
