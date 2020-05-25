# Life in Picture

This is python Web app made with the Django froma work that enables the user to upload images as they see fit. Classification is based on category and location.Other people can view them and are also able to copy an image url which can be shared on other platforms.

### User Stories:
1. View different photos that interest me.
1. Click on a single photo to expand it and also view the details of the photo. The photo details must appear on a modal within the same route as the main page.
1. Search for different categories of photos. (e.g. Travel, Food)
1. Copy a link to the photo to share with my friends.
1. View photos based on the location they were taken.


## Set up and Installation
### Prerequisites
The user will require git, django, postgres and python3.6+ installed in their machine.
To install these two, you can use the following commands
```
#git
$ sudo apt install git-all

#python3.6
$ sudo apt-get install python3.6.

#django
$ pip install django==3.0.6

#postgres
$ pip install psycopg2 
```
### Requirements
1. asgiref==3.2.7
1. astroid==2.4.1
1. beautifulsoup4==4.9.1
1. Django==3.0.6
1. django-bootstrap4==1.1.1
1. isort==4.3.21
1. lazy-object-proxy==1.4.3
1. mccabe==0.6.1
1. Pillow==7.1.2
1. psycopg2==2.8.5
1. pylint==2.5.2
1. pyperclip==1.8.0
1. python-decouple==3.3
1. pytz==2020.1
1. six==1.15.0
1. soupsieve==2.0.1
1. sqlparse==0.3.1
1. toml==0.10.1
1. typed-ast==1.4.1
1. wrapt==1.12.1
### .ENV file
1. SECRET_KEY='<SECRET_KEY>'
1. DEBUG=True #set to false in production
1. DB_NAME='databasename'
1. DB_USER='username'
1. DB_PASSWORD='password'
1. DB_HOST='127.0.0.1'
1. MODE='dev' #set to 'prod' in production
1. ALLOWED_HOSTS='.localhost', '.herokuapp.com', '.127.0.0.1'
1. DISABLE_COLLECTSTATIC=1

### Installation
1. To access this application on your command line, you need to clone it 
`https://github.com/martyminion/PersonalGallery.git`
1. Create a requirements.txt in the root folder and copy the requirements above.
1. Install the required technologies with
`pip install -r requirements.txt`
1. Create a .env file and copy the .env code above
1. You can then run the server with:
`python3.6 manage.py runserver`
1. You can make changes to the db with
`python3.6 manage.py makemigrations photos`
`python3.6 manage.py migrate`
4. You can run tests:
`python3.6 manage.py test photos`


### Break down into end to end tests
### Example
  ```
    def test_delete_image(self):
    '''
    tests if an image instance is deleted
    '''
    image_2 = Image(image_url = "path/to/images/new", name = "The Genting", description = "A family day",locations = self.new_location , categories = self.new_category)
    image_2.save_image()
    image_2.delete_image()
    result=Image.get_image_by_id(id = image_2.id)
    self.assertEqual(result,"Image does not exist")
  ```
* The above test checks whether the delete method works and confirms that on look up it is not there  

## Bugs
  No known bugs as of yet, if encountered you can get me on *martyminion0@gmail* or log an issue from github

## Deployment

The app can be found live on heroku: https://lifeinpicture.herokuapp.com/
Refresh the page for Masonry Grid to take good effect

## Built With

* Python 3.6.9 
* Django Framework 3.0
* JavaScript and JQuery
* HTML and CSS

## Authors

* **Martin Kimani** 

## License

This project is licensed under the GNU License - see the [LICENSE.md](LICENSE.md) file for details
Copyright{ 2020 }

