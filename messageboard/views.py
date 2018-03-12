from django.shortcuts import render
from django.http import HttpResponse

from . import models


def index(request):
    article = models.Aticle.objects.get(pk=1)
    return render(request, 'messageboard/index.html', {'article' : article})
