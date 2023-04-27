from .models import Post,PostComment,PostImage,PostReplay,PostLike
from rest_framework import serializers
from djoser.serializers import UserSerializer as BaseUserSerializer, UserCreateSerializer as BaseUserCreateSerializer


class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLike
        fields = ['id']
     
    def create(self, validated_data):
        user_id = self.context['user_id']
        post_id = self.context['post_id']
        if PostLike.objects.filter(post_id=post_id).filter(user_id=user_id).exists():
            raise serializers.ValidationError(
                'You have already liked this post.')
        return PostLike.objects.create(post_id=post_id,user_id=user_id, **validated_data)
    
    
    
class CommentReplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = PostReplay
        fields = ['id', 'created_at', 'text']     
        
    def create(self, validated_data):
        comment_id = self.context['comment_id']
        return PostReplay.objects.create(comment_id=comment_id, **validated_data)
    
    
    
class PostCommentSerializer(serializers.ModelSerializer):
    replays = CommentReplaySerializer(many= True,read_only= True)
    id = serializers.IntegerField(read_only= True)
    class Meta:
        model = PostComment
        fields = ['id', 'created_at', 'text','replays']

    def create(self, validated_data):
        post_id = self.context['post_id']
        return PostComment.objects.create(post_id=post_id, **validated_data)



class PostImageSerializer(serializers.ModelSerializer): 
    
    class Meta: 
        model = PostImage 
        fields = ['id', 'image']   
        
    def create(self, validated_data): 
        pid=self.context['post_id'] 
        return PostImage.objects.create(post_id=pid,**validated_data)
   


class PostSerializer(serializers.ModelSerializer):
    images = PostImageSerializer(many= True,read_only= True)
    comments = PostCommentSerializer(many= True,read_only= True)
    likes_count = serializers.IntegerField(read_only=True)
    replays = CommentReplaySerializer(many= True,read_only= True)
    
    class Meta:
        model = Post
        fields = ['id','title', 'slug','categories', 'last_update',
                  'created_at','images','comments','likes_count','replays']


        
class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'username', 'password',
                  'email', 'first_name', 'last_name']



class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
        


        
     
