from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *
from django.http import JsonResponse
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin
from django.contrib.auth import get_user_model


class CreateUserView(CreateModelMixin, GenericViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserLoginSerializer
    permission_classes =  [permissions.AllowAny]


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['username'] = user.username
        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


#takes a list of http actions we can send to this view
@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token',
        '/api/token/refresh'
    ]
    return Response(routes)

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

class likeStoryViewSet(viewsets.ModelViewSet):
    queryset = likeStory.objects.all()
    serializer_class = StoryLikeSerializer
    permission_classes = [permissions.IsAuthenticated]

class NotificationViewSet(viewsets.ModelViewSet):
    serializer_class =NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]


    
    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Notification.objects.all().filter(seen = False)
        userID = self.request.query_params.get('userID')
        if userID is not None:
            queryset = queryset.filter(user = userID)
        return queryset
          

class StoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Story.objects.all()
    serializer_class = StorySerializer
    permission_classes = [permissions.IsAuthenticated]

class StoryListByTopic(viewsets.ModelViewSet):

    serializer_class = StorySerializer
    permission_classes = [permissions.IsAuthenticated]

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


class StoryLikedByUser(viewsets.ModelViewSet):
    serializer_class = StoryLikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = likeStory.objects.all()
        userID = self.request.query_params.get('userID')
        if userID is not None:
            queryset = queryset.filter(user = userID)
        return queryset



class StoryLikedByStory(viewsets.ModelViewSet):
    serializer_class = StoryLikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = likeStory.objects.all()
        storyID = self.request.query_params.get('storyID')
        if storyID is not None:
            queryset = queryset.filter(story = storyID)
        return queryset



class FeedListByTopic(viewsets.ModelViewSet):

    serializer_class = FeedSerializer
    permission_classes = [permissions.IsAuthenticated]


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
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer
    permission_classes = [permissions.IsAuthenticated]




class CommentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]


class StoryCommentViewSet(viewsets.ModelViewSet):

    queryset = StoryComment.objects.all()
    serializer_class = StoryCommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = StoryComment.objects.all()
        storyID = self.request.query_params.get('storyID')
        if storyID is not None:
            queryset = queryset.filter(story = storyID)
        return queryset



class TopicRankingViewSet(viewsets.ModelViewSet):

    serializer_class = TopicRankingSerializer
    permission_classes = [permissions.IsAuthenticated]
    topN = 4

    def get_queryset(self):
        queryset = TopicRanking.objects.all()[:self.topN]
        return queryset

