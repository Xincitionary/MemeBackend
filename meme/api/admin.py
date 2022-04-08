from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from .forms import UserLoginCreationForm, UserLoginChangeForm

#https://learndjango.com/tutorials/django-custom-user-model

# Register your models here.
# admin.site.register(UserLogin)
# admin.site.register(UserInfo)

from django.apps import apps

class CustomUserAdmin(UserAdmin):
    add_form = UserLoginCreationForm
    form = UserLoginChangeForm
    model = UserLogin
    list_display = ["email", "username",]

admin.site.register(UserLogin, CustomUserAdmin)

models = apps.get_models()

for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass