from app.models import Author, Blog, Comment
from app.api.serializers import AuthorSerializer
from rest_framework import mixins,generics

#API for Listing Authors
class AuthorsListView(generics.ListAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()