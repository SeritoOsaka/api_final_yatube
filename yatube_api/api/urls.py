from api.views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet
from django.urls import include, path
from rest_framework import routers

API_VERSION = 'v1/'

router_version_1 = routers.DefaultRouter()
router_version_1.register('posts', PostViewSet, basename='posts')
router_version_1.register(
    r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comments'
)
router_version_1.register('groups', GroupViewSet, basename='groups')
router_version_1.register('follow', FollowViewSet, basename='follow')

urlpatterns = [
    path(API_VERSION, include(router_version_1.urls)),
    path(API_VERSION, include('djoser.urls')),
    path(API_VERSION, include('djoser.urls.jwt'))
]
