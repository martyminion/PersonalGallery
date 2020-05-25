from django.test import TestCase
from .models import Location,Tags,Category,Image
from django.core.exceptions import ObjectDoesNotExist

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
    image = Image.get_image_by_id(self.new_image.id)

    self.assertEqual(image,self.new_image)

  def test_save_image(self):
    '''
    test to chack if an image is saved in the database
    '''
    new_image2 = Image(image_url = "path/to/new/imag", name = "Genting Highlands Mall", description = "A day in the lagoon",locations = self.new_location , categories = self.new_category)
    new_image2.save_image()
    self.assertTrue(len(Image.objects.all())>1)
  
  def test_update_image_description(self):
    '''
    test to update the location of an image
    '''
    new_descr = "Family above all"
    # Image.update_image_description(1,new_descr)
    new_image2 = Image(image_url = "path/to/new/imag", name = "Genting Highlands Mall", description = "A day in the lagoon",locations = self.new_location , categories = self.new_category)
    new_image2.save_image()
    Image.update_image_description(self.new_image.id,new_descr)
    new_im = Image.get_image_by_id(self.new_image.id)
    self.assertEqual(new_im.description,"Family above all")
    
  def test_image_by_location(self):
    '''
    test to see if images can be returned by location
    '''
    location_images = Image.image_by_location(self.new_location)
    self.assertTrue(len(location_images)>0)
    for location_image in location_images:
      self.assertEqual(location_image.locations,self.new_location)

  def test_search_by_category(self):
    '''
    tests to see if a search returns the searched images
    '''
    categoryimages = Image.search_by_category(self.new_category)
    for categoryimage in categoryimages:
      self.assertEqual(categoryimage.categories,self.new_category)

  def test_search_by_tags(self):
    '''
    tests to see if a search returns the searched images
    '''
    tagimages = Image.search_by_tags(self.new_tag)
    self.assertTrue(len(tagimages)>0)
  
  def test_delete_image(self):
    '''
    tests if an image instance is deleted
    '''
    image_2 = Image(image_url = "path/to/images/new", name = "The Genting", description = "A family day",locations = self.new_location , categories = self.new_category)
    image_2.save_image()
    image_2.delete_image()
    result=Image.get_image_by_id(id = image_2.id)
    self.assertEqual(result,"Image does not exist")

'''
Tests on Category Model
'''
class CategoryTest(TestCase):
  '''
  This class defines the test cases for the Category model
  '''
  def setUp(self):
    '''
    this function runs at the beginning of each test
    '''
    self.new_category2 = Category(name = "Nature")

  def test_save_category(self):
    '''
    this test confirms if the function works
    '''
    self.new_category2.save_category()
    nature = Category.objects.get(name = "Nature")
    self.assertEqual(nature,self.new_category2)
    self.new_category2.delete()

  def test_delete_category(self):
    '''
    this test checks if the item will be deleted
    '''
    self.new_category2.save_category()
    self.new_category2.delete_category()
    
    categorynumber = len(Category.objects.all())
    self.assertTrue(categorynumber == 0)
    
  def test_update_category(self):
    '''
    this test checks if the name is updated to new value
    '''
    self.new_category2.save_category()
    self.new_category2.update_category("Booze")
    new_booze = Category.objects.get(name = "Booze")
    self.assertEqual(new_booze.name,"Booze")
'''
Tests on Location Model
'''
class LocationTest(TestCase):
  '''
  This class defines the test cases for the Category model
  '''
  def setUp(self):
    '''
    this function runs at the beginning of each test
    '''
    self.new_location2 = Location(city = "Nairobi", country = "Kenya", specific_locale = "Waterefrom Karen")
    
  def test_save_location(self):
    '''
    this test confirms if the function works
    '''
    self.new_location2.save_location()
    nairobi = Location.objects.get(city = "Nairobi")
    self.assertEqual(nairobi,self.new_location2)
    self.new_location2.delete()

  def test_delete_location(self):
    '''
    this test checks if the item will be deleted
    '''
    self.new_location2.save_location()
    self.new_location2.delete_location()
    locationnumber = len(Location.objects.all())
    self.assertTrue(locationnumber == 0)
    
  def test_update_location(self):
    '''
    this test checks if the name is updated to new value
    '''
    self.new_location2.save_location()
    self.new_location2.update_location("Naivas Supermarket")
    new_locale = Location.objects.get(specific_locale = "Naivas Supermarket")
    self.assertEqual(new_locale.specific_locale,"Naivas Supermarket")

