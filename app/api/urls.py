from django.urls import path
from app.api.views import AuthorsListView, AuthorBlogsView, BlogsListView, BlogDetailView

urlpatterns = [
    path('authors/',AuthorsListView.as_view()),
    path('author/<int:pk>/blogs',AuthorBlogsView.as_view()), 
    path('blogs/',BlogsListView.as_view()),
    path('blog/<int:pk>/',BlogDetailView.as_view()),
]