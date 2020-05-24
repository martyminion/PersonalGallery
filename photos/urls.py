from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('',views.homepage, name='homePage'),
  path('search/tags',views.search_tags,name='searchTags'),
  path('copy/image/<int:imageid>',views.copy_image_url,name='copyUrl'),
  path('locations/',views.location,name='locations'),
  path('categories/',views.categories, name='categories')

]
if settings.DEBUG:
  urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)