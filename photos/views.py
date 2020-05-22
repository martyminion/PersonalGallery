from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homepage(request):
  '''
  This view function will show a random display of images from the database
  '''
  title = "See"
  
  return render(request,'home.html',{"title":title})