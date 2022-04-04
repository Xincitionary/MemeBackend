"""meme URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()

router.register(r'userLogin', views.UserLoginViewSet)
router.register(r'userInfo', views.UserInfoViewSet)
router.register(r'Topics', views.TopicViewSet)
router.register(r'Comments', views.CommentViewSet)
router.register(r'PostListByTopic', views.StoryListByTopic, basename = 'StoryListByTopic')
router.register(r'PostListByUser', views.FeedListByTopic, basename = 'FeedListByUser')
router.register(r'topicRanking',views.TopicRankingViewSet,basename = 'topicRankingList' )
router.register(r'filteredPostList', views.FilteredPostList, basename = 'filteredPostList')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls'))
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
] + router.urls




