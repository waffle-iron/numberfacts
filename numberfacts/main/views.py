# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

from main.models import Number, Fact

def homepage(request):
    #return HttpResponse("hello nerd")
    print "hi im in the views"
    numbers = Number.objects.all()
    context = {
        "numbers": numbers,
    }
    return render(request, "main/homepage.html",context)

def view_number(request, number_get):
    context = {
        "foo": "bar",
    }
    print type(number_get)
    the_number = Number.objects.get(number = number_get)
    print type(the_number)

    # -- add the number to the context
    context['the_number'] = the_number

    print context

    return render(request, "main/view_number.html",context)
