from django.http import HttpResponse
from django.shortcuts import render


def app01(request):
    return render(request, 'app01.html')


def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    return render(request, 'index.html')


def trade(request):
    pass

def choose_st(request):
    pass


def maalarm(request):
    if request.method=='GET':
        return render(request, 'maalarm.html')
    maalarm = request.POST.get('maalarm', '')
    name = request.POST.get('name', '')
    bar = request.POST.getlist('bar', [])
    return HttpResponse('提交成功')


def matrade(request):
    return render(request, 'matrade.html')
