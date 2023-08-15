from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path("", home, name="home"),
    path("post/", PostListView.as_view(), name="post_list"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post_details"),
    path("categories/", category_list, name="category_list"),
    path("categories/<int:pk>/", category_details, name="category_details"),
    path("comment_update/<int:pk>", CommentUpdateView.as_view(), name="comment_update"),
]
