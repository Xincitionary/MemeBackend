from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .models import *
from .serializers import *

# Create your views here.



class UserLoginViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = UserLogin.objects.all()
    serializer_class = UserLoginSerializer
    permission_classes = [permissions.IsAuthenticated]


class TopicViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = [permissions.IsAuthenticated]



class UserInfoViewSet(viewsets.ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer
    permission_classes = [permissions.IsAuthenticated]





class StoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Topic.objects.all()
    serializer_class = StorySerializer
    permission_classes = [permissions.IsAuthenticated]



class StoryListByTopic(viewsets.ModelViewSet):

    serializer_class = StorySerializer


    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Story.objects.all()
        topicID = self.request.query_params.get('topicID')
        if topicID is not None:
            queryset = queryset.filter(topic = topicID)
        return queryset


class FeedListByTopic(viewsets.ModelViewSet):

    serializer_class = FeedSerializer


    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Feed.objects.all()
        topicID = self.request.query_params.get('topicID')
        if topicID is not None:
            queryset = queryset.filter(topic = topicID)
        return queryset


class FeedViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Topic.objects.all()
    serializer_class = FeedSerializer
    permission_classes = [permissions.IsAuthenticated]



class CommentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]



class CommentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]


        
class TopicRankingViewSet(viewsets.ModelViewSet):

    serializer_class = TopicRankingSerializer
    permission_classes = [permissions.IsAuthenticated]
    topN = 4

    def get_queryset(self):
        queryset = TopicRanking.objects.all()[:self.topN]
        return queryset


#By default in the frontend, everything should be included. 
class FilteredPostList(viewsets.ModelViewSet):

    serializer_class= StorySerializer
    permission_classes = [permissions.IsAuthenticated]

    # Need to define a serializer class 
    def get_queryset(self):
        queryset_Feed = Feed.objects.all()
        queryset_Story = Feed.objects.all()
        include_shared = self.request.query_params.get('include_shared')  
        # include_comment = self.request.query_params.get('include_comment')  
        include_anonymous = self.request.query_params.get('include_shared')  
        start_time = self.request.query_params.get('start_time')
        finish_time = self.request.query_params.get('finish_time')

        if not (include_shared):  #if we don't include shared post. 
            queryset_Feed.filter(parentFeed = None)
            queryset_Story.filter(parent = None)
        if not (include_anonymous):
            queryset_Feed.filter(anonymous = 0)
            queryset_Story.filter(anonymous = 0)
        queryset_Feed.filter(create_time__gte= start_time, create_time__lte=finish_time)
        queryset_Story.filter(create_time__gte= start_time, create_time__lte=finish_time)
        return queryset_Story

