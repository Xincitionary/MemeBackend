from django.db import models

#on_delete: https://stackoverflow.com/questions/38388423/what-does-on-delete-do-on-django-models
#meta: https://docs.djangoproject.com/en/4.0/ref/models/options/

# Create your models here.
class UserLogin(models.Model):
    # UserLogin_id = models.AutoField(primary_key=True, unique = True)
    username = models.CharField(max_length=36)
    password = models.CharField(max_length=36)
    create_time = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'UserLogin'
        managed = False
    def __str__(self):
        return f"{self.id}: {self.username}"


class Topic(models.Model):
    #topic id
    creatorID =models.ForeignKey(UserLogin, models.CASCADE)
    num_followers = models.IntegerField()
    num_feeds = models.IntegerField()
    num_stories = models.IntegerField()
    trending = models.BooleanField()
    topicName = models.CharField(max_length = 45)
    abstract = models.CharField(max_length=200)
    class Meta:
        db_table = 'Topic'
        managed = False
    def __str__(self):
        ret = "the topic title is " + self.topicName
        return ret


class UserPost(models.Model):
    visibility = models.CharField(max_length=36)
    anonymous = models.BooleanField()
    view_count = models.IntegerField()
    topicID = models.ForeignKey(Topic, on_delete = models.CASCADE)
    userID =  models.ForeignKey(UserLogin, on_delete = models.CASCADE)
    parentID = models.ForeignKey('self',on_delete = models.CASCADE)
    is_story = models.BooleanField()
    class Meta:
        db_table = 'Posts'
        managed = False
    def __str__(self):
        return f"{self.id}: {self.username}"


#child of the topic class 
class Story(models.Model):
    storyID = models.OneToOneField(
        UserPost,
        on_delete= models.CASCADE,
        primary_key= True,
    )
    content = models.CharField(max_length=1000)
    class Meta:
        db_table = 'Stories'
        managed = False


#child of the topic class 
class Feed(models.Model):
    storyID = models.OneToOneField(
        UserPost,
        on_delete= models.CASCADE,
        primary_key= True,
    )
    content = models.CharField(max_length=200)
    emoji = models.IntegerField()
    class Meta:
        db_table = 'Feeds'
        managed = False