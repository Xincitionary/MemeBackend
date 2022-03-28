from django.db import models
from django.utils import timezone

#on_delete: https://stackoverflow.com/questions/38388423/what-does-on-delete-do-on-django-models
#meta: https://docs.djangoproject.com/en/4.0/ref/models/options/

# Create your models here.
class User(models.Model):
    userID =  models.AutoField(primary_key=True, verbose_name="pk_user", default=-1)
    username = models.CharField(max_length=36)
    password = models.CharField(max_length=36)
    create_time = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'User'

    def __str__(self):
        return f"{self.id}: {self.username}"


