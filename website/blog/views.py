from .models import Post
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
# rest api imports
from website import serializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from user.models import Profile
from rest_framework.exceptions import PermissionDenied



class PostListView(ListView):
    model = Post
    ordering = ['-date']
    paginate_by = 5
        
      
           
    


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'post_image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UserListView(ListView):
    model = Post
    context_object_name = 'posts'

    paginate_by = 5
    template_name = 'blog/user_post.html'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date')


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'post_image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDetailView(DetailView):
    model = Post

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


# rest api 

class PostListCreateViewApi(generics.ListCreateAPIView):
    
    def get_permissions(self):
        if self.request.method == "POST":
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = []  
        
        return super().get_permissions()

    
    def get_serializer_class(self):
        if self.request.method == "GET":
            return serializer.PostGetSerializer
        elif self.request.method == "POST":
            return serializer.PostSerializer
    
    def get(self, request, *args, **kwargs):
        self.serializer_class = self.get_serializer_class()
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.serializer_class = self.get_serializer_class()
        return self.create(request, *args, **kwargs)

    
    # permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    
    
    
    def perform_create(self, serializer):
        print(self.request.user)
        serializer.save(author=self.request.user)
        
       
class ProfileListViewApi(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
   
    serializer_class = serializer.ProfileSeralizer
    
    def get_queryset(self):
        userz = self.request.user
        return Profile.objects.filter(user=userz)

class ProfileUpdateViewApi(generics.UpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = serializer.ProfileUpdateSerializer
    permission_classes = [IsAuthenticated] 
    def get_object(self):
        user = self.request.user
        profile = user.profile
        self.kwargs['pk'] = profile.pk
        return super().get_object()
    def perform_update(self, serializer):
        name = User.objects.get(email=self.request.user.email)
        name.username = self.request.data['username']
        name.save()
        serializer.save()  
       
    
       
        
class PostDetailViewApi(generics.RetrieveAPIView):
    permission_classes =[IsAuthenticated()]
    queryset = Post.objects.all()
    serializer_class = serializer.PostSerializer
    
    
class PostUpdateViewApi(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = serializer.PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save()  

    def get_object(self):
        obj = super().get_object()
       
        if obj.author != self.request.user:
            raise PermissionDenied()
        return obj        

class PostDeleteViewApi(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = serializer.PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_destroy(self, instance):
        instance.delete()

    def get_object(self):
        obj = super().get_object()
       
        if obj.author != self.request.user:
            raise PermissionDenied()
        return obj        
    
class UserPostListViewApi(generics.ListAPIView):
    serializer_class = serializer.PostSerializer

    def get_queryset(self):
        author_id = self.kwargs['author_id']
        return Post.objects.filter(author_id=author_id)

class UserCreateListViewApi(generics.ListCreateAPIView):
    
    def get_permissions(self):
        if self.request.method == "POST":
            self.permission_classes = [] 
        else:
            self.permission_classes = [IsAuthenticated] 
        
        return super().get_permissions()

    def get_queryset(self):
        user = self.request.user.username
        return User.objects.filter(username=user)
    
    def get_serializer_class(self):
        if self.request.method == "GET":
            return serializer.UserListSerializer
        elif self.request.method == "POST":
            return serializer.UserCreateSerializer
    
    def get(self, request, *args, **kwargs):
        self.serializer_class = self.get_serializer_class()
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.serializer_class = self.get_serializer_class()
        return self.create(request, *args, **kwargs)

    
            