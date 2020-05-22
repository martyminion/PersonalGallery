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
    #image
    new_image = Image(image_url = "path/to/imag", name = "Dubai Mall", description = "A lively night out",
        locations = "Dubai", categories = "Travel", tags = "food")
    #tags
    new_tag = Tags(name = "food")
    #categories
    new_category = Category(name = "Travel")
    #location
    new_location = Location(city = "Dubai", country = "UAE", specific_locale = "Dubai Mall Waterfront")

    new_location.save()
    new_category.save()
    new_tag.save()
    new_image.save()

  '''
  Tests
  '''

  def test_instance(self):
    '''
    Test to see if instantiation was correct
    '''
    self.assertTrue(isinstance(self.new_image,Image))

  def test_get_image_by_id(self,id):
    '''
    Test to check if function can return correct data
    '''
    image = Image.get_image_by_id(1)
    self.assertEqual(image,self.new_image)

