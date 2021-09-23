from django.urls import path, include
from rest_framework.routers import SimpleRouter

from api.views import CommentViewSet, PostViewSet, GroupViewSet, FollowViewSet


router = SimpleRouter()

router.register('posts', PostViewSet, basename='post')
router.register('groups', GroupViewSet, basename='group')
router.register('follow', FollowViewSet, basename='follow')
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comment')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
