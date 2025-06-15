from django.urls import path
from . import views

app_name = 'core'
urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('post/create/', views.create_post, name='create_post'),
    path('post/<int:post_id>/like/', views.like_post, name='like_post'),
    path('user/<int:user_id>/follow/', views.follow_user, name='follow_user'),
    path('post/<int:post_id>/comment/', views.comment_post, name='comment_post'),
    path('post/<int:post_id>/share/', views.share_post, name='share_post'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('post/<int:post_id>/delete/', views.delete_post, name='delete_post'),
    path('post/<int:post_id>/edit/', views.edit_post, name='edit_post'),
    path('search/', views.search, name='search'),
]