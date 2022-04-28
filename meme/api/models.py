from unittest.mock import DEFAULT
from django.db import models
from django.contrib.auth.models import AbstractUser #,PermissionMixin
from django.conf import settings
# from datetime import datetime

#on_delete: https://stackoverflow.com/questions/38388423/what-does-on-delete-do-on-django-models
#meta: https://docs.djangoproject.com/en/4.0/ref/models/options/
#blank and null: https://stackoverflow.com/questions/8609192/what-is-the-difference-between-null-true-and-blank-true-in-django

# Create your models here.

class UserLogin(AbstractUser):
    pass

    def __str__(self):
        return f"{self.id}: {self.username}"


class UserInfo(models.Model):
    id = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='UserInfo_id'
    )
    gender = models.CharField(max_length=15)
    bio = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    school = models.CharField(max_length=45)
    degree = models.CharField(max_length=45)
    num_following = models.IntegerField()
    num_followers = models.IntegerField()
    trophy = models.CharField(max_length=45)
    wechat = models.CharField(max_length=45)
    instagram = models.CharField(max_length=45)
    profile_pic = models.CharField(max_length= 100, default = "none")
    verified = models.BooleanField()

    def __str__(self):
        return f"{self.id}: {self.bio}"

class UserFollowing(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="following", on_delete=models.CASCADE)
    following = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="followers", on_delete=models.CASCADE)


class Topic(models.Model):
    #topic id
    creator =models.ForeignKey(settings.AUTH_USER_MODEL,null =True, on_delete=models.SET_NULL)
    create_time = models.DateTimeField(auto_now_add=True)
    last_updated =  models.DateTimeField(auto_now=True)
    num_followers = models.IntegerField()
    num_feeds = models.IntegerField()
    num_stories = models.IntegerField()
    trending = models.BooleanField()
    topicName = models.CharField(max_length = 45)
    abstract = models.CharField(max_length=200)

    def __str__(self):
        ret = "the topic title is " + self.topicName
        return ret

class TopicModerator(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="moderator", on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, related_name="topicModerated", on_delete = models.CASCADE)


class FollowTopic(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="userFollowing", on_delete = models.CASCADE)
    topic = models.ForeignKey(Topic, related_name="topicFollowed", on_delete = models.CASCADE)



#abstract class Post; no table created.
class Post(models.Model):
    visibility = models.CharField(max_length=36, blank = True)
    anonymous = models.BooleanField(default=1, blank = True)
    view_count = models.IntegerField(default=0,blank = True)
    create_time = models.DateTimeField(auto_now_add=True)
    topic = models.ForeignKey(Topic, null=True, on_delete = models.CASCADE)
    user =  models.ForeignKey(settings.AUTH_USER_MODEL,null=True, on_delete = models.CASCADE)
    num_comments = models.IntegerField(default=0, blank = True)
    num_shares = models.IntegerField(default=0, blank = True)
    num_likes = models.IntegerField(default=0, blank = True)
    location = models.CharField(max_length=100, blank = True, null = True)
    username = models.CharField(max_length=150, blank = True, null = True, default = "匿名")


    class Meta:
        ordering = ['-create_time']
        abstract = True


# #child of the topic class 
class Story(Post):
    class Exist(models.TextChoices):
        EXIST = 'EXIST','EXIST'
        EXISTED = "EXISTED",'EXISTED'
       

    Exist = models.CharField(
        max_length=7,
        choices=Exist.choices,
        default=Exist.EXIST
    )
    title = models.CharField(max_length=100,null = True,blank=True)
    content = models.CharField(max_length=1000)
    DateHappened = models.CharField(max_length=15,blank= True, null=True)
    parent = models.ForeignKey('self',null = True,blank=True, on_delete = models.SET_NULL, related_name="parentStoryS")
    # liked_by = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='likedByUser')

    def __str__(self):
        return f"{self.id}: {self.content}"


# #child of the topic class 
class Feed(Post):

    content = models.CharField(max_length=200, blank = True)
    emoji = models.IntegerField(default = 0, blank = True)
    parentFeed = models.ForeignKey('self',null = True,blank=True, on_delete = models.SET_NULL, related_name="parentFeedF")
    parentStory = models.ForeignKey(Story,null = True,blank=True, on_delete = models.SET_NULL, related_name="parentStoryF")
    parentIsStory = models.BooleanField(default=None, null= True)


    def __str__(self):
        return f"{self.id}: {self.content}"


#comments for the feeds class 
class Comment(models.Model):
    content = models.CharField(max_length=300)
    create_time =models.DateTimeField(auto_now_add=True)
    emoji = models.IntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE)
    parent = models.ForeignKey('self',null = True,blank=True, on_delete = models.SET_NULL)

    def __str__(self):
        return f"{self.id}: {self.content}"

#Topics that are yet to added.
class TopicRanking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='topicCreator')
    create_time = models.DateTimeField(auto_now_add=True)
    topicName= models.CharField(max_length=45)
    topicAbstract = models.CharField(max_length=255)
    moderator = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='topicModerator')
    votes = models.IntegerField()

    class Meta:
        ordering = ['-votes']

    def __str__(self):
        return f"{self.id}: {self.topicName}"

class Question(models.Model):
    questionContent =  models.CharField(max_length= 255)

class userResponse(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)
    user= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.id}: {self.topicName}"


class invite_code(models.Model):
    inviteID= models.CharField(max_length = 20, primary_key= True)
    taken = models.BooleanField()

    def __str__(self):
        return f"{self.id}: {self.taken}"

class likeStory(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="userLiking", on_delete = models.CASCADE)
    story = models.ForeignKey(Story, related_name="storyLiked", on_delete = models.CASCADE)

