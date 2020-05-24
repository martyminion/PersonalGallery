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
    return self.city

  def delete_location(self):
    self.delete()

  def update_location(self,new_locale):
    '''
    This function updates the category name
    '''
    Location.objects.filter(id = self.id).update(specific_locale = new_locale)


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
    This function adds a new category into the database
    '''
    self.save()

  def delete_category(self):
    '''
    This function deletes a category from the database
    '''
    self.delete()

  def update_category(self,new_name):
    '''
    This function updates the category name
    '''
    Category.objects.filter(id = self.id).update(name = new_name)

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
    This function adds a tag into the database
    '''
    self.save()

  def delete_tag(self):
    '''
    This function deletes a tag from the database
    '''
    self.delete()

  def update_tag(self,new_name):
    '''
    This function updates the tag name
    '''
    Tags.objects.filter(id = self.id).update(name = new_name)


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
  picha_image = models.ImageField(upload_to='photos/')

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

 
  def delete_image(self):
    '''
    This function deletes an image from the data base
    '''
    self.delete()
   

  @classmethod
  def update_image_description(cls,id,new_description):
    '''
    this functions updates the location of the image
    '''
    image_update = cls.get_image_by_id(id)
    if image_update == "Image does not exist":
      message = "Image does not exist"
      return message
    else:
      Image.objects.filter(id=id).update(description = new_description)
      message = "Successfull update"
      return message
  @classmethod
  def image_by_location(cls,location):
    '''
    this function returns images based on the location
    '''
    try:
      images_by_location = cls.objects.filter(locations = location).all()
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
      searched_images = cls.objects.filter(categories = search_term)
      return searched_images
    except ObjectDoesNotExist:
      message = "We could not find any photos of that category"
      return message

  @classmethod
  def search_by_tags(cls,search_term):
    try:
      searched_images = cls.objects.filter(tags = search_term)
      return searched_images
    except ObjectDoesNotExist:
      message = "We could not find any photos with that tag"
      return message