from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Image,Tags,Category,Location
import pyperclip
from django.views.decorators.clickjacking import xframe_options_sameorigin
# Create your views here.

def homepage(request):
  '''
  This view function will show a random display of images from the database
  '''
  title = "Home"
  most_images = Image.objects.order_by('-id').all()[:10]
  
  return render(request,'home.html',{"title":title,"images":most_images})

def search_tags(request):
  '''
  this will return search results based on the tags
  '''
  title = "search results"
  if 'searchtag' in request.GET and request.GET["searchtag"]:
    search_tag = request.GET.get("searchtag")
    tags = Tags.objects.all()
    for tag in tags:
      if tag.name==search_tag:
        search_results = Image.search_by_tags(tag)
        if len(search_results) > 0:
          return render(request,'search_results.html',{"title":title,"search_results":search_results,"search_term":search_tag})
        else:
          message_noimage = "There is no image with that tag"
          return render(request,'search_results.html',{"message":message_noimage,"title":title,"search_term":search_tag})

      else:
        message_notag = "There is no tag with that name" 
    else:
      return render(request,'search_results.html',{"message":message_notag,"title":title})
  else:
    message = "You haven't searched for any images"
    return render(request,'search_results.html',{"message":message,"title":title})  
    

def copy_image_url(request,imageid):
  '''
  copies the image url
  '''
  copyimage = Image.get_image_by_id(imageid)
  image_url = copyimage.copy_imageurl()
  pyperclip.copy(image_url)
  return redirect('/')

def location(request):
  '''
  this view function shows all the availale locations
  '''
  title = "locations"
  all_locations = Location.objects.all()
  return render(request,'locations.html',{"title":title,"all_locations"=all_locations}) 

def categories(request):
  '''
  this view function shows all te available categories
  '''
  title = "categories"
  all_categories = Category.objects.all()
  return render(request,'categories.html',{"title":title,"all_categories"=all_categories})
  

def show_category_images(request,cat_name):
  '''
  this function displays the images from a particular category
  '''
  title = cat_name
  cat_results = Image.search_by_category(cat_name)

def show_location_images(request,loc_name):
  '''
  this function displays the images from a particular location
  '''
  title = loc_name
  loc_results = Image.image_by_location(loc_name)

  