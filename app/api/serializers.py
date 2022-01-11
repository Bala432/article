from rest_framework import serializers
from app.models import Author, Blog, Comment

#Mapping Blog Model to a Serializer
class BlogSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Blog
        exclude = ('author','id')
        
#Mapping Author Model to a Serializer
class AuthorSerializer(serializers.ModelSerializer):
    # blog = BlogSerializer(many=True,read_only=True)
    class Meta:
        model = Author
        fields = "__all__"
        
