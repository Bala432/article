from django.urls import path
from app.api.views import AuthorsListView, AuthorBlogsView

urlpatterns = [
    path('authors/',AuthorsListView.as_view()),
    path('author/<int:pk>/blogs',AuthorBlogsView.as_view()), 
]