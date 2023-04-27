from django.urls import path
from django.urls.conf import include
from rest_framework_nested import routers
from . import views


router = routers.DefaultRouter()
router.register('posts', views.PostViewSet, basename='posts')


posts_router = routers.NestedDefaultRouter(router, 'posts', lookup='post')
posts_router.register('images', views.PostImageViewSet, basename='post-images')
posts_router.register('comments', views.CommentViewSet, basename='post-comments')
posts_router.register('likes', views.LikeViewSet, basename='post-comments')


comments_router = routers.NestedDefaultRouter(posts_router, 'comments', lookup='comment')
comments_router.register('replays', views.ReplayViewSet, basename='comment-replays')


# urlpatterns = [ 
#                path('',include(router.urls)), 
#                path('',include(posts_router.urls)),
#                path('',include(comment_router.urls)),]

urlpatterns = router.urls + posts_router.urls + comments_router.urls
