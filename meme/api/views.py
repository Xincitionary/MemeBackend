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



# class PostListByTopic(viewsets.ModelViewSet):

#     serializer_class = PostSerializer


#     def get_queryset(self):
#         """
#         Optionally restricts the returned purchases to a given user,
#         by filtering against a `username` query parameter in the URL.
#         """
#         queryset = Post.objects.all()
#         topicID = self.request.query_params.get('topicID')
#         if topicID is not None:
#             queryset = queryset.filter(topic = topicID)
#         return queryset


# class PostListByUser(viewsets.ModelViewSet):

#     serializer_class = PostSerializer


#     def get_queryset(self):
#         """
#         Optionally restricts the returned purchases to a given user,
#         by filtering against a `username` query parameter in the URL.
#         """
#         queryset = Post.objects.all()
#         creator = self.request.query_params.get('userID')
#         if creator is not None:
#             queryset = queryset.filter(user = creator)
#         return queryset


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


