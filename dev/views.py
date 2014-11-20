from django.shortcuts import render
from django.template import RequestContext, loader


def index(request):
    template = loader.get_template('index.html')
    context = RequestContext(request, {
        'name': 'ursa-django',
    })
    return HttpResponse(template.render(context))
