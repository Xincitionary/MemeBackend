from pyexpat import model
from api.models  import *
from rest_framework import serializers

class UserLoginSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserLogin
        fields = ['id','username','password','last_login','date_joined','email']



class UserInfoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = UserInfo
        fields = ['gender','bio','school','degree','num_following','num_followers','trophy','wechat','instagram','verified','user_id']
        # depth = 1

class TopicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Topic
        fields = ['id', 'creator','num_followers','num_feeds','num_stories','trending', 'abstract', 'topicName', 'create_time','last_updated']

class StorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Story
        fields = ['id','title','content','visibility','anonymous','view_count','create_time','parent_id','topic_id','user_id','num_comments']

    
class FeedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Feed
        fields =['id','emoji','content','visibility','anonymous','view_count','create_time','parentFeed_id','parentStory_id','topic_id','user_id']

    
class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ['id','create_time','content','emoji','parent_id','user_id','feed_id']


class TopicRankingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TopicRanking
        fields =['id','create_time','topicName','topicAbstract','votes','moderator_id','user_id']

        
class FilteredSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    topic = serializers.IntegerField(read_only=True)
    # create_time = serializers.DateTimeField()