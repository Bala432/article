from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
class Blog(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=1000)
    type = models.CharField(max_length=20)
    author = models.ForeignKey(Author,on_delete=models.CASCADE,related_name="blog")
    
    def __str__(self):
        return self.title + " by "+ str(self.author)
    
class Comment(models.Model):
    comment = models.TextField(max_length=100)
    like = models.BooleanField(default=False)
    dislike = models.BooleanField(default=False)
    number_of_likes = models.PositiveIntegerField(default=0)
    number_of_dislikes = models.PositiveIntegerField(default=0)
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE,related_name="comments")
    
    def __str__(self):
        return self.comment + " for " + self.blog