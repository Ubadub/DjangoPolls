from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from polls.models import Question, Choice

def homepage(request):
	questions = Question.objects.all()
	return HttpResponse("Hello world! Welcome to the polls app!")