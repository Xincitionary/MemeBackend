from pyexpat import model
from api.models  import *
from rest_framework import serializers
from django.contrib.auth import get_user_model 


class UserLoginSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(write_only=True)
    
    def create(self, validated_data):
        user = UserLogin.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email = validated_data['email'],
            gender = validated_data['gender'],
            social_media = validated_data['social_media']
        )

        return user
    class Meta:
        model = UserLogin
        fields = ['id','username','password','last_login','date_joined','email','gender', 'social_media']

        # extra_kwargs ={
        #     'password':{'write_only':True}
        # }


class NotificationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'user_id','profile_pic','create_time','message','seen','story_id','username','Action']



class UserInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserInfo
        fields = ['gender','bio','school','degree','profile_pic','num_following','num_followers','trophy','wechat','instagram','verified','user_id']
        # depth = 1

class TopicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Topic
        fields = ['id', 'creator','member_action','topic_color','requires_address','num_followers','num_feeds','num_stories','trending', 'abstract', 'topicName', 'button_prompt','create_time','last_updated']

class StorySerializer(serializers.HyperlinkedModelSerializer):
    topic_id = serializers.IntegerField()
    parent_id= serializers.IntegerField()
    user_id= serializers.IntegerField()

    class Meta:
        model = Story
        fields = ['id','title','content','username','DateHappened','location','lon','lat','popup_note','Exist','visibility','anonymous','view_count','create_time','parent_id','topic_id','user_id','num_comments', 'num_shares','num_likes']


    def create(self, validated_data):
        topic = validated_data.pop('topic_id')
        user = validated_data.pop('user_id')
        parent = validated_data.pop('parent_id')
        story_instance = Story.objects.create(**validated_data, topic_id=topic, user_id = user, parent_id = parent)
        
        return story_instance


class StoryLikeSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField()
    story_id = serializers.IntegerField()

    class Meta:
        model = likeStory
        fields =( 'id','story_id','user_id')

    def create(self, validated_data):
        story = validated_data.pop('story_id')
        user = validated_data.pop('user_id')
        like_instance = likeStory.objects.create(**validated_data, story_id=story, user_id = user)
        return like_instance
        
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



class StoryCommentSerializer(serializers.HyperlinkedModelSerializer):
    user_id = serializers.IntegerField()
    story_id = serializers.IntegerField()
    parent_id = serializers.IntegerField()
    class Meta:
        model = StoryComment
        fields = ['id','create_time','content','anonymous','emoji','parent_id','user_id','story_id', 'username']


    def create(self, validated_data):
        user = validated_data.pop('user_id')
        parent = validated_data.pop('parent_id')
        story = validated_data.pop('story_id')
        story_instance = StoryComment.objects.create(**validated_data, story_id = story, user_id = user, parent_id = parent)
        
        return story_instance



class TopicRankingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TopicRanking
        fields =['id','create_time','topicName','topicAbstract','votes','moderator_id','user_id']

