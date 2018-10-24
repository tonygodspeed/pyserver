# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return render(request,'t1.html')

def add(request):
    a = request.GET['a'];
    b = request.GET['b'];
    c = int(a) + int(b);
    return HttpResponse(str(c))

def add2(request,a,b):
    c = int(a) + int(b);
    return HttpResponse(str(c))