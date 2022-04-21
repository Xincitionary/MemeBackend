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
    topic_id = serializers.IntegerField()
    parent_id= serializers.IntegerField()
    user_id= serializers.IntegerField()
    class Meta:
        model = Story
        fields = ['id','title','content','visibility','anonymous','view_count','create_time','parent_id','topic_id','user_id','num_comments', 'num_shares','num_likes']

    def create(self, validated_data):
        topic = validated_data.pop('topic_id')
        user = validated_data.pop('user_id')
        parent = validated_data.pop('parent_id')

        story_instance = Story.objects.create(**validated_data, topic_id=topic, user_id = user, parent_id = parent)
        return story_instance



class FeedSerializer(serializers.ModelSerializer):
    topic_id = serializers.IntegerField()
    parentFeed_id = serializers.IntegerField()
    parentStory_id= serializers.IntegerField()
    user_id= serializers.IntegerField()
    class Meta:
        model = Feed
        fields= ('topic_id','id','emoji','content','visibility','anonymous','view_count','create_time','parentFeed_id','parentStory_id','user_id','num_comments', 'num_shares','num_likes')
 

    def create(self, validated_data):
        topic = validated_data.pop('topic_id')
        user = validated_data.pop('user_id')
        parentFeed = validated_data.pop('parentFeed_id')
        parentStory =validated_data.pop('parentStory_id')
        feed_instance = Feed.objects.create(**validated_data, topic_id=topic, user_id = user, parentFeed_id = parentFeed, parentStory_id = parentStory)
        return feed_instance

    
class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ['id','create_time','content','emoji','parent_id','user_id','feed_id']


class TopicRankingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TopicRanking
        fields =['id','create_time','topicName','topicAbstract','votes','moderator_id','user_id']

