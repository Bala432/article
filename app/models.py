from django.db import models
from django.contrib.auth.models import User
    
class Blog(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=1000)
    type = models.CharField(max_length=20)
    blog_created_time = models.DateTimeField(auto_now_add=True)
    blog_updated_time = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name="blog")
    number_of_likes = models.PositiveIntegerField(default=0)
    number_of_dislikes = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.title + " by "+ str(self.author)
    
class Comment(models.Model):
    review_author = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name='review_author')
    comment = models.TextField(max_length=100)
    comment_created_time = models.DateTimeField(auto_now_add=True)
    comment_updated_time = models.DateTimeField(auto_now=True)
    like = models.BooleanField(default=False)
    dislike = models.BooleanField(default=False)
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE,related_name="comments")
    
    def __str__(self):
        return self.comment + " for " + str(self.blog)