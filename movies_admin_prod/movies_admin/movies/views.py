from django.http import HttpResponse
from django.shortcuts import render


def sample_view(request):
    html = '<body><h1>Django sample_view</h1><br><p>Отладка sample_view</p></body>'
    return HttpResponse(html)
