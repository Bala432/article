from rest_framework.exceptions import ValidationError
from app.models import Author, Blog, Comment
from app.api.serializers import AuthorSerializer, BlogSerializer
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status

#API for Listing Authors
class AuthorsListView(ListAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    
#API for Listing Blogs of Author
class AuthorBlogsView(ListAPIView):
    serializer_class = BlogSerializer
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        try:
            author = Author.objects.get(pk=pk)
        except:
            raise ValidationError({'Invalid Request': 'Author doesnot exist'})
        return Blog.objects.filter(author=author)
    
#API for Listing All blogs
class BlogsListView(ListAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
    
#API for Details of Specific Blog
class BlogDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
    
    # def get_queryset(self):
    #     pk = self.kwargs['pk']
    #     try:
    #         blog = Blog.objects.get(pk=pk)
    #         print('blog is ',blog)
    #     except Blog.DoesNotExist:
    #         raise ValidationError({'Invalid Request': 'Blog doesnot exist'})
    #     return Blog.objects.get(pk=pk)
            