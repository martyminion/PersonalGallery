from django.test import TestCase
from .models import Location,Tags,Category,Image

# Create your tests here.

class ImageTest(TestCase):
  '''
  This class defines the test cases for the Image model
  '''
  def setUp(self):
    '''
    This function runs at the beginning of every test
    '''
    
   
    #tags
    self.new_tag = Tags(name = "food")
    
    #categories
    self.new_category = Category(name = "Travel")
    #location
    self.new_location = Location(city = "Dubai", country = "UAE", specific_locale = "Dubai Mall Waterfront")
    #image
    self.new_image = Image(image_url = "path/to/imag", name = "Dubai Mall", description = "A lively night out",locations = self.new_location , categories = self.new_category)
        
   
    self.new_location.save()
    self.new_category.save()
    self.new_tag.save()
    self.new_image.save()
    self.new_image.tags.add(self.new_tag)

  '''
  Tests
  '''

  def test_instance(self):
    '''
    Test to see if instantiation was correct
    '''
    self.assertTrue(isinstance(self.new_image,Image))

  def test_get_image_by_id(self):
    '''
    Test to check if function can return correct data
    '''
    image = Image.get_image_by_id(1)
    self.assertEqual(image,self.new_image)

