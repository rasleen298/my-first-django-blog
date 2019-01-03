from django.contrib import admin

# Register your models here.
from .models import Post  #imports our post from models.py


admin.site.register(Post)
'''
    As you can see, we import (include) the Post model defined in the previous chapter.
    To make our model visible on the admin page, we need to register the model with admin.site.register(Post).
    '''
