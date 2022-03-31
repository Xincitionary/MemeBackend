from api.models  import *
from rest_framework import serializers

class UserLoginSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserLogin
        fields = ['id','username','password','create_time']

class TopicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Topic
        fields = ['id', 'creatorID','num_followers','num_feeds','num_stories','trending', 'abstract', 'topicName']

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'visibility','anonymous','view_count','create_time','is_story','parent_id','topic_id','user_id']



class StorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Story
        fields = ['id','title','content']

    
class FeedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Feed
        fields = ['id','emoji','content']