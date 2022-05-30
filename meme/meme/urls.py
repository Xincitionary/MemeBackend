
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from api import views


router = routers.DefaultRouter()

router.register(r'createuser', views.CreateUserView, basename = 'createUser')
router.register(r'userLogin', views.UserLoginViewSet, basename = 'userlogin')
router.register(r'userInfo', views.UserInfoViewSet, basename = 'userinfo')
router.register(r'Topics', views.TopicViewSet, basename = 'Topics')
router.register(r'Comments', views.CommentViewSet, basename='comments')
router.register(r'StoryComments', views.StoryCommentViewSet, basename='StoryComments')
router.register(r'Notifications',views.NotificationViewSet, basename = 'notifications')
router.register(r'Feeds',views.FeedViewSet,basename = 'Feeds')
router.register(r'Storys',views.StoryViewSet,basename = 'Stories')
router.register(r'StoryListByTopic', views.StoryListByTopic, basename = 'StoryListByTopic')
router.register(r'FeedListByTopic', views.FeedListByTopic, basename = 'FeedListByTopic')
router.register(r'topicRanking',views.TopicRankingViewSet,basename = 'topicRanking' )
router.register(r'StoryLikedByUser',views.StoryLikedByUser,basename = 'StoryLikedByUser' )
router.register(r'StoryLikedByStory',views.StoryLikedByStory,basename = 'StoryLikedByStory' )
router.register(r'likeStoryViewSet',views.likeStoryViewSet, basename='likeStoryViewSet')




urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls'))
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
] + router.urls


urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
