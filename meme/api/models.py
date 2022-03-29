from django.db import models
from django.utils import timezone

#on_delete: https://stackoverflow.com/questions/38388423/what-does-on-delete-do-on-django-models
#meta: https://docs.djangoproject.com/en/4.0/ref/models/options/

# Create your models here.
class UserLogins(models.Model):
    # userID = models.AutoField(primary_key=True, unique = True)
    username = models.CharField(max_length=36)
    password = models.CharField(max_length=36)
    create_time = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'UserLogin'

    def __str__(self):
        return f"{self.id}: {self.username}"


