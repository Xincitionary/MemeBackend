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
