from django.contrib import admin
from .models import Tags,Image,Category,Location
# Register your models here.
admin.site.register(Tags)
admin.site.register(Image)
admin.site.register(Category)
admin.site.register(Location)