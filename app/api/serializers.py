from rest_framework import serializers
from app.models import Author, Blog, Comment

#Mapping Author Model to a Serializer
class AuthorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Author
        fields = "__all__"