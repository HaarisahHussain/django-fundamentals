from lib2to3.fixes.fix_input import context
from tempfile import template

from django.http import HttpResponse
from django.shortcuts import render

from meetings.models import Meeting, Room

#Function is used when user visits welcome page and sends the string to the user


def welcome(request):
    return render(request,template_name="website/welcome.html",
    context={"meetings": Meeting.objects.all()})


def about(request):
    return HttpResponse("My Name is Haarisah and I like cats >.<")

