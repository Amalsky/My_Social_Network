
from django.contrib import admin
from django.conf import settings
from django.urls import path,include
from user import views as user_views
from django.conf.urls.static import static
from django.contrib.auth import  views as auth_views
from blog import views as blog_views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path("", include('blog.url')),
    path('fav/<int:id>/', user_views.favourite_add, name='favourite_add'),
    path('profile/fav/', user_views.favourite_list, name='favourite_list'),
    path("admin/", admin.site.urls),
    path("profile/",user_views.profile,name='profile'),
    path("register/", user_views.register,name='register'),
    path("login/", auth_views.LoginView.as_view(template_name='user/login.html'),name='login'),
    path("logout/", auth_views.LogoutView.as_view(template_name='user/logout.html'),name='logout'),
    path("logout/", auth_views.LogoutView.as_view(template_name='user/logout.html'),name='logout'),
    path("password_reset/", auth_views.PasswordResetView.as_view(template_name='user/password_reset.html'),name='password_reset'),
    path("password_reset/done/", auth_views.PasswordResetDoneView.as_view(template_name='user/password_reset_done.html'),name='password_reset_done'),
    path("password_reset_confirm/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name='user/password_reset_confirm.html'),name='password_reset_confirm'),
    path("password_reset_complete/", auth_views.PasswordResetCompleteView.as_view(template_name='user/password_reset_complete.html'),name='password_reset_complete'),
    
    #rest api urls
    
    #provide auth token
    path("api/post_auth_token/", obtain_auth_token,name='post_auth_token'),
    
    # user signup api createing a user  listing all details of loged in user
    path("api/user/signup/",blog_views.UserCreateListViewApi.as_view(),name='post_auth_token'),
    
    # post create and list api(you can create a post user must be logged in, you can list all posts in the wedbsite no authotication need )
    path("api/post_create_list/", blog_views.PostListCreateViewApi.as_view(),name='post_api_create_list'),
    
    # post detail api you can get the pk  from list view(api/post_create_list/, method=get)  copy past the id 
     path("api/post/detail/<int:pk>/", blog_views.PostDetailViewApi.as_view(),name='post_api_detail'),
     
     # post update api  user must be logged in and he must be the author of the post 
     path("api/post/update/<int:pk>/", blog_views.PostUpdateViewApi.as_view(),name='post_api_update'),
     
     path("api/post/delete/<int:pk>/", blog_views.PostDeleteViewApi.as_view(),name='post_api_delete'),
     
     # listing post by an indual author pass the author id(can be obtain from  (api/post_create_list, method=get) )
     path("api/post/user/<int:author_id>/", blog_views.UserPostListViewApi.as_view(),name='post_user_list'),
     
    
    # Profile list api get logged in userprofile
     path("api/profile_create_list/", blog_views.ProfileListViewApi.as_view(),name='Profile_api_create_list'),
     
     # profile edit api
     path("api/profile/update/", blog_views.ProfileUpdateViewApi.as_view(),name='Profile_upate_api'),
    

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)