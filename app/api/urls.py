from django.urls import path
from app.api.views import ( UsersListView, UserBlogsView, BlogsListView, BlogCreateView,
                            BlogDetailView, CommentsListView, CommentDetailView, registration_view, login_view )
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('users/',UsersListView.as_view()),
    # path('user/<int:pk>/blogs',UserBlogsView.as_view()), 
    path('user/blogs',UserBlogsView.as_view()), 
    path('blogs/',BlogsListView.as_view()),
    path('create-blog/',BlogCreateView.as_view()),
    path('blog/<int:pk>/',BlogDetailView.as_view()),
    path('blog/<int:pk>/comments',CommentsListView.as_view()),
    path('blog/comment/<int:pk>',CommentDetailView.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/',registration_view),
    path('login/',login_view),
]