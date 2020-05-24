from django.shortcuts import render
from django.http import HttpResponse
from .models import Image,Tags,Category,Location

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
  
    