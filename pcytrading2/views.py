from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    # return HttpResponse("Hello world ! ")
    context = {}
    context['hello'] = 'kw hello  ni hao '
    return render(request, 'hello.html', context)

