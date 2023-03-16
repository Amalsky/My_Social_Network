from . import views
from django.urls import path

urlpatterns = [
    path("", views.PostListView.as_view(),name='home'),
    path("new/", views.PostCreateView.as_view(),name='new'),
    path("post/<int:pk>/update//", views.PostUpdateView.as_view(),name='update'),
    path("post/<int:pk>/detail/", views.PostDetailView.as_view(),name='detail'),
    path("post/<int:pk>/delete/", views.PostDeleteView.as_view(),name='delete'),
    path("user/<str:username>", views.UserListView.as_view(),name='user-post'),
]
