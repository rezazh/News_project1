from django.shortcuts import render
from .models import Post, PostImage, PostComment, PostReplay, PostLike
from .serializers import PostSerializer, PostImageSerializer, PostCommentSerializer, CommentReplaySerializer, \
    PostLikeSerializer
from rest_framework.response import Response
from django.db.models.aggregates import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny


class PostViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete', 'head', 'options']

    def get_permissions(self):
        if self.request.method in ['PATCH', 'DELETE']:
            return [IsAdminUser()]
        if self.request.method in ['GET']:
            return [AllowAny()]
        return [IsAuthenticated()]

    queryset = Post.objects.prefetch_related('images').all().annotate(likes_count=Count('posts')).all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['title']
    ordering_fields = ['last_update']

    def get_serializer_context(self):
        return {'request': self.request}


class PostImageViewSet(ModelViewSet):
    serializer_class = PostImageSerializer
    http_method_names = ['get', 'post', 'patch', 'delete', 'head', 'options']

    def get_permissions(self):
        if self.request.method in ['PATCH', 'DELETE']:
            return [IsAdminUser()]
        return [IsAuthenticated()]

    def get_serializer_context(self):
        return {'post_id': self.kwargs['post_pk']}

    def get_queryset(self):
        return PostImage.objects.filter(post_id=self.kwargs['post_pk'])


class CommentViewSet(ModelViewSet):
    serializer_class = PostCommentSerializer
    http_method_names = ['get', 'post', 'patch', 'delete', 'head', 'options']

    def get_permissions(self):
        if self.request.method in ['PATCH', 'DELETE']:
            return [IsAdminUser()]
        return [IsAuthenticated()]

    def get_queryset(self):
        return PostComment.objects.filter(post_id=self.kwargs['post_pk'])

    def get_serializer_context(self):
        return {'post_id': self.kwargs['post_pk']}


class ReplayViewSet(ModelViewSet):
    serializer_class = CommentReplaySerializer
    http_method_names = ['get', 'post', 'patch', 'delete', 'head', 'options']

    def get_permissions(self):
        if self.request.method in ['PATCH', 'DELETE']:
            return [IsAdminUser()]
        return [IsAuthenticated()]

    def get_queryset(self):
        return PostReplay.objects.filter(comment_id=self.kwargs['comment_pk']).filter(
            comment_id__post_id=self.kwargs['post_pk'])

    def get_serializer_context(self):
        return {'comment_id': self.kwargs['comment_pk']}


class LikeViewSet(ModelViewSet):
    serializer_class = PostLikeSerializer
    http_method_names = ['get', 'post', 'delete', 'head', 'options']

    def get_permissions(self):
        if self.request.method in ['PATCH', 'DELETE']:
            return [IsAdminUser()]
        return [IsAuthenticated()]

    def get_queryset(self):
        return PostLike.objects.filter(post_id=self.kwargs['post_pk'])

    def get_serializer_context(self):
        return {'post_id': self.kwargs['post_pk'], 'user_id': self.request.user.id}
