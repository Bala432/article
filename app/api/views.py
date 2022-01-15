from rest_framework.exceptions import ValidationError
from app.models import User, Blog, Comment
from app.api.serializers import UserSerializer, BlogSerializer, CommentSerializer
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework.views import APIView

#API for Logging User
@api_view(['POST'])
def login_view(request):
    
    if request.method == 'POST':
        username = request.data['username']
        password = request.data['password']
        
        user = authenticate(username=username, password=password)
        if user is None:
            raise ValidationError("Invalid username/password. Please try again!")
        account = User.objects.get(username=username)
        data = {}
        data['response'] = 'Login Succesfull'
        data['username'] = account.username
        refresh_token = RefreshToken.for_user(account)
        data['token'] = {
            'access_token': str(refresh_token.access_token),
            'refresh_token' : str(refresh_token)
        }
        return Response({'success':'Sucessfully authenticated'})

#API for Registering Users
@api_view(['POST'])
def registration_view(request):
    
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        data = {}
        
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'Registration Succesfull'
            data['username'] = account.username
            refresh_token = RefreshToken.for_user(account)
            data['token'] = {
                'access_token': str(refresh_token.access_token),
                'refresh_token' : str(refresh_token)
            }
            
        else:
            data = serializer.errors
        return Response(data)

#API for Listing Users
class UsersListView(ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    
#API for Listing Blogs of User
class UserBlogsView(ListAPIView):
    serializer_class = BlogSerializer
    
    def get_queryset(self):
        user_blogs = Blog.objects.filter(author=self.request.user)
        if user_blogs is None:
            raise ValidationError({'Empty Blogs': 'User had not produced any Blog'})
        return user_blogs
    
#API for Listing All blogs
class BlogsListView(ListAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
    
#API for Details of Specific Blog
class BlogDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
    
#API for Creating Blogs
class BlogCreateView(APIView):
    
    
    def post(self, request):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=self.request.user)
            return Response(serializer.data)
        return Response(serializer.errors)
    
#API for Listing Comments for a specific Blog
class CommentsListView(ListAPIView):
    serializer_class = CommentSerializer
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        blog = Blog.objects.get(pk=pk)
        return Comment.objects.filter(blog = blog)
    
#API for Detailing Comments
class CommentDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()