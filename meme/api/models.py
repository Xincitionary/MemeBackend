from django.db import models

#on_delete: https://stackoverflow.com/questions/38388423/what-does-on-delete-do-on-django-models
#meta: https://docs.djangoproject.com/en/4.0/ref/models/options/
#blank vs null: https://stackoverflow.com/questions/8609192/what-is-the-difference-between-null-true-and-blank-true-in-django

# Create your models here.
class UserLogin(models.Model):
    username = models.CharField(max_length=36)
    password = models.CharField(max_length=36)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id}: {self.username}"



#
class UserInfo(models.Model):
    email = models.CharField(max_length=255)
    gender = models.CharField(max_length=15)
    bio = models.CharField(max_length=100)
    userID = models.ForeignKey(UserLogin, on_delete = models.CASCADE)
    school = models.CharField(max_length=45)
    degree = models.CharField(max_length=45)
    num_following = models.IntegerField()
    num_followers = models.IntegerField()
    trophy = models.CharField(max_length=45)
    wechat = models.CharField(max_length=45)
    instagram = models.CharField(max_length=45)
    verified = models.BooleanField()

    def __str__(self):
        return f"{self.id}: {self.bio}"

class UserFollowing(models.Model):
    userID = models.ForeignKey(UserLogin, related_name="following", on_delete=models.CASCADE)
    followingID = models.ForeignKey(UserLogin, related_name="followers", on_delete=models.CASCADE)


class Topic(models.Model):
    #topic id
    creatorID =models.ForeignKey(UserLogin, on_delete=models.CASCADE)
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
    userID = models.ForeignKey(UserLogin, related_name="moderator", on_delete=models.CASCADE)
    topicID = models.ForeignKey(Topic, related_name="topicModerated", on_delete = models.CASCADE)


class FollowTopic(models.Model):
    userID = models.ForeignKey(UserLogin, related_name="userFollowing", on_delete = models.CASCADE)
    topicID = models.ForeignKey(Topic, related_name="topicFollowed", on_delete = models.CASCADE)



#abstract class Post; no table created.
class Post(models.Model):
    visibility = models.CharField(max_length=36)
    anonymous = models.BooleanField()
    view_count = models.IntegerField()
    topicID = models.ForeignKey(Topic, on_delete = models.CASCADE)
    userID =  models.ForeignKey(UserLogin, on_delete = models.CASCADE)
    parentID = models.ForeignKey('self',on_delete = models.CASCADE)
    is_story = models.BooleanField()

    def __str__(self):
        return f"{self.id}: {self.username}"
    class Meta:  #abstract class refer: https://docs.djangoproject.com/en/4.0/topics/db/models/#abstract-base-classes
        abstract = True



# #child of the topic class 
class Story(Post):
    content = models.CharField(max_length=1000)
    def __str__(self):
        return f"{self.id}: {self.content}"

# #child of the topic class 
class Feed(Post):
    content = models.CharField(max_length=200)
    emoji = models.IntegerField()
    def __str__(self):
        return f"{self.id}: {self.content}"


#comments for the feeds class 
class Comments(models.Model):
    content = models.CharField(max_length=300)
    create_time =models.DateTimeField(auto_now_add=True)
    emoji = models.IntegerField()
    userID = models.ForeignKey(UserLogin, on_delete=models.CASCADE)
    feedID = models.ForeignKey(Feed, on_delete=models.CASCADE)
    parentID = models.ForeignKey('self',on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}: {self.content}"


class TopicRanking(models.Model):
    userID = models.ForeignKey(UserLogin, on_delete=models.CASCADE, related_name='topicCreator')
    create_time = models.DateTimeField(auto_now_add=True)
    topicName= models.CharField(max_length=45)
    topicAbstract = models.CharField(max_length=255)
    moderatorID = models.ForeignKey(UserLogin,on_delete=models.CASCADE,related_name='topicModerator')
    votes = models.IntegerField()

    class Meta:
        ordering = ['votes']

    def __str__(self):
        return f"{self.id}: {self.topicName}"

class Question(models.Model):
    questionContent =  models.CharField(max_length= 255)

class userResponse(models.Model):
    questionID = models.ForeignKey(Question, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)
    userID= models.ForeignKey(UserLogin, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.id}: {self.topicName}"


class invite_code(models.Model):
    inviteID= models.CharField(max_length = 20, primary_key= True)
    taken = models.BooleanField()

    def __str__(self):
        return f"{self.id}: {self.taken}"
