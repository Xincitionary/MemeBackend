from pyexpat import model
from api.models  import *
from rest_framework import serializers

class UserLoginSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserLogin
        fields = ['id','username','password','create_time']



class UserInfoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = UserInfo
        fields = ['email','gender','bio','school','degree','num_following','num_followers','trophy','wechat','instagram','verified','user_id']
        # depth = 1

class TopicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Topic
        fields = ['id', 'creator','num_followers','num_feeds','num_stories','trending', 'abstract', 'topicName', 'create_time','last_updated']

class StorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Story
        fields = ['id','title','content']

    
class FeedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Feed
        fields = ['id','emoji','content']

    
class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ['id','create_time','content','emoji','parent_id','user_id','feed_id']