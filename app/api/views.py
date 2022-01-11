from rest_framework.exceptions import ValidationError
from app.models import Author, Blog, Comment
from app.api.serializers import AuthorSerializer, BlogSerializer
from rest_framework import mixins,generics
from rest_framework.response import Response
from rest_framework import status

#API for Listing Authors
class AuthorsListView(generics.ListAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    
#API for Listing Blogs of Author
class AuthorBlogsView(generics.ListAPIView):
    serializer_class = BlogSerializer
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        try:
            author = Author.objects.get(pk=pk)
        except:
            raise ValidationError({'Invalid Request': 'Author doesnot exist'})
        return Blog.objects.filter(author=author)
    
            