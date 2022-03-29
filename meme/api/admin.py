from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(UserLogin)
admin.site.register(Topic)
admin.site.register(UserPost)
admin.site.register(Story)
admin.site.register(Feed)