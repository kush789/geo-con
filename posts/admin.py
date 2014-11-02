from django.contrib import admin
from posts.models import *

# Register your models here.

Models = [Post,Comment, Like, CLike, Follow, Stalk]

admin.site.register(Models)







