# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render

from .models import Station


def index(request):

    context = {

    }
    return render(request, 'polls/index.html', context)


def heatmap(request):

    context = {

    }
    return render(request, 'polls/heatmap.html',context)

def searchbus(request):

    context = {

    }
    return render(request, 'polls/SEARCH_BUS.html',context)

def numofeverday(request):

    context = {

    }
    return render(request, 'polls/NumofEverday.html',context)
def numofhour_sum(request):

    context = {

    }
    return render(request, 'polls/numofhour.html',context)
def numofhour_everday(request):

    context = {
    }
    return render(request, 'polls/NumOfHourInEverday.html',context)
def locationwithtime(request):

    context = {
    }
    return render(request, 'polls/locWithTime_diffcolor.html',context)

def pieofmes(request):

    context = {
    }
    return render(request, 'polls/pieOfMes.html',context)

#######################################################
def num(request):

    context = {
    }
    return render(request, 'polls/Num.html',context)
