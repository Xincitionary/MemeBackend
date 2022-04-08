
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from api import views


router = routers.DefaultRouter()

router.register(r'userLogin', views.UserLoginViewSet)
router.register(r'userInfo', views.UserInfoViewSet)
router.register(r'Topics', views.TopicViewSet)
router.register(r'Comments', views.CommentViewSet)
router.register(r'StoryListByTopic', views.StoryListByTopic, basename = 'StoryListByTopic')
router.register(r'FeedListByTopic', views.FeedListByTopic, basename = 'FeedListByTopic')
router.register(r'topicRanking',views.TopicRankingViewSet,basename = 'topicRanking' )
router.register(r'filteredPostList', views.FilteredPostListViewSet, basename = 'filteredPostList')




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
