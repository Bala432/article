from django.urls import path
from app.api.views import AuthorsListView

urlpatterns = [
    path('authors/',AuthorsListView.as_view())    
]