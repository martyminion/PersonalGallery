from django.db import models
from django.core.exceptions import ObjectDoesNotExist

# Create your models here.
class Location(models.Model):
  '''
  this class defines the attributes of a location
  '''
  city = models.CharField(max_length=30)
  country = models.CharField(max_length=30)
  specific_locale = models.CharField(max_length=30, null=True)

  
  def save_location(self):
    '''
    This function adds an image into the database
    '''
    self.save()

  def __str__(self):
    '''
    this function returns a stringified name of the object i.e. when looking up 
    the object instance of the class and getting Location 1 you'll instead get the 
    spsecified return value
    '''
    return self.name

  def delete_category(self):
    self.delete()

class Category(models.Model):
  '''
  this class the attributes  of a category
  '''
  name = models.CharField(max_length=30)

  def __str__(self):
    '''
    this function returns a stringified name of the object i.e. when looking up 
    the object instance of the class and getting Category 1 you'll instead get the 
    spsecified return value
    '''
    return self.name

  def save_category(self):
    '''
    This function adds an image into the database
    '''
    self.save()

  def delete_category(self):
    self.delete()

class Tags(models.Model):
  '''
  this class defines the different tags an image can have
  '''
  name = models.CharField(max_length=30, default="no Tag")

  def __str__(self):
    '''
    this function returns a stringified name of the object i.e. when looking up 
    the object instance of the class and getting Tags 1 you'll instead get the 
    spsecified return value
    '''
    return self.name

  def save_tag(self):
    '''
    This function adds an image into the database
    '''
    self.save()

  def delete_category(self):
    self.delete()

class Image(models.Model):
  '''
  This class defines the attributes of an image
  '''
  image_url = models.CharField(max_length=100)
  name = models.CharField(max_length=50)
  description = models.CharField(max_length=100,null=True)
  locations = models.ForeignKey(Location, on_delete = models.CASCADE)
  categories = models.ForeignKey(Category, on_delete = models.CASCADE)
  tags = models.ManyToManyField(Tags)

  def __str__(self):
    '''
    this function returns a stringified name of the object i.e. when looking up 
    the object instance of the class and getting Image 1 you'll instead get the 
    spsecified return value
    '''
    return self.name

  @classmethod
  def get_image_by_id(cls,id):
    '''
    This function return a single image using its id
    '''
    try:
      new_img = cls.objects.get(id = id)
      return new_img
    except ObjectDoesNotExist:
      message = "Image does not exist"
      return message
    
  
  def save_image(self):
    '''
    This function adds an image into the database
    '''
    self.save()

  @classmethod
  def delete_image(cls,id):
    '''
    This function deletes an image from the data base
    '''
    image_delete = cls.get_image_by_id(id=id)
    if image_delete == "Image does not exist":
      message = "Image does not exist"
      return message
    else:
      image_delete.delete()
      message = "Successfull deletion"
      return message

  @classmethod
  def update_image_location(cls,id,new_description):
    '''
    this functions updates the location of the image
    '''
    image_update = cls.get_image_by_id(id)
    if image_update == "Image does not exist":
      message = "Image does not exist"
      return message
    else:
      image_update.update(description = new_description)
      message = "Successfull update"
      return message
  @classmethod
  def image_by_location(cls,location):
    '''
    this function returns images based on the location
    '''
    try:
      images_by_location = cls.objects.filter(location__icontains = location).all()
      return images_by_location
    except ObjectDoesNotExist:
      message = "There are no images from that location"
      return message
    else:
      message = "Sorry we could not understand that request"
      return message 
   
  @classmethod
  def search_by_category(cls,search_term):
    try:
      searched_images = cls.objects.filter(tags__icontains = search_term)
      return searched_images
    except ObjectDoesNotExist:
      message = "We could not find any photos with that tag"
      return message