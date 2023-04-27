from django.db import models
from django.contrib.auth.models import User,AbstractUser
from django.conf import settings


# class User(AbstractUser):
    
#     email = models.EmailField(unique=True)
    # user = models.OneToOneField(User,on_delete=models.CASCADE)

    

class Post(models.Model):
    title = models.CharField(max_length=120)
    categories = models.CharField(max_length=120)
    details = models.TextField(null=True, blank= True)
    slug = models.SlugField(unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    # featured_likes = models.ForeignKey(
    #     'PostLike', on_delete=models.SET_NULL, null=True, related_name='+', blank=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['created_at']



class PostImage(models.Model): 
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name = 'images')
    image = models.ImageField(upload_to='core/images')


    
class PostComment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
    
    
    
class PostReplay(models.Model):
    comment = models.ForeignKey(PostComment, on_delete=models.CASCADE,related_name= 'replays')
    text = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:100]
    


class PostLike(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='users')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='posts')
    
    class Meta:
        unique_together=[['user','post']]