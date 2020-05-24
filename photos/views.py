from django.shortcuts import render
from django.http import HttpResponse
from .models import Image,Tags,Category,Location

# Create your views here.

def homepage(request):
  '''
  This view function will show a random display of images from the database
  '''
  title = "Home"
  most_images = Image.objects.order_by('id').all()[:10]
  
  return render(request,'home.html',{"title":title,"images":most_images})