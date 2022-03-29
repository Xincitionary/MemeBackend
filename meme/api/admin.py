from django.contrib import admin
from .models import *

# Register your models here.
# admin.site.register(UserLogin)
# admin.site.register(UserInfo)
# admin.site.register(Topic)
# admin.site.register(UserPost)
# admin.site.register(Story)
# admin.site.register(Feed)

from django.apps import apps

models = apps.get_models()

for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass