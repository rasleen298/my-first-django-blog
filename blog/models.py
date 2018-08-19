from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
	author=models.ForeignKey('auth.User',on_delete=models.CASCADE)
	title=models.CharField(max_length=200) #charfield takes a limit of text
	text=models.TextField()					#textfield takes text without limit
	created_date=models.DateTimeField(default=timezone.now)
	published_date=models.DateTimeField(blank=True,null=True)

	def publish(self):
		self.published_date=timezone.now()
		self.save()
	
	def __str__(self):				#double underscore=dunder
		return self.title

#now add model to our database
'''The last step here is to add our new model to our database. First we have to make Django know that we have some changes in our model. (We have just created it!) Go to your console window and type python manage.py makemigrations blog. It will look like this:

command-line
(myvenv) ~/djangogirls$ python manage.py makemigrations blog
Migrations for 'blog':
  blog/migrations/0001_initial.py:
  - Create model Post
'''
##########
'''Django prepared a migration file for us that we now have to apply to our database. Type python manage.py migrate blog and the output should be as follows:

command-line
(myvenv) ~/djangogirls$ python manage.py migrate blog
Operations to perform:
  Apply all migrations: blog
Running migrations:
  Applying blog.0001_initial... OK
  '''