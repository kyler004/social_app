from django.db import models
"""
This module defines the core models for a simple social media application.
Models:
    Post: Represents a user-created post, which may contain text content and an optional image.
    Like: Represents a 'like' relationship between a user and a post, ensuring a user can like a post only once.
    Follow: Represents a 'follow' relationship between two users, ensuring a user can follow another user only once.
    Comment: Represents a comment made by a user on a post.
Classes:
    Post(models.Model):
        Fields:
            user (ForeignKey): The user who created the post.
            content (TextField): The textual content of the post.
            image (ImageField): Optional image associated with the post.
            created_at (DateTimeField): Timestamp when the post was created.
        Methods:
            __str__: Returns a string representation of the post.
    Like(models.Model):
        Fields:
            user (ForeignKey): The user who liked the post.
            post (ForeignKey): The post that was liked.
            created_at (DateTimeField): Timestamp when the like was created.
        Meta:
            unique_together: Ensures a user can like a post only once.
        Methods:
            __str__: Returns a string representation of the like.
    Follow(models.Model):
        Fields:
            follower (ForeignKey): The user who is following another user.
            followed (ForeignKey): The user being followed.
            created_at (DateTimeField): Timestamp when the follow was created.
        Meta:
            unique_together: Ensures a user can follow another user only once.
        Methods:
            __str__: Returns a string representation of the follow relationship.
    Comment(models.Model):
        Fields:
            user (ForeignKey): The user who made the comment.
            post (ForeignKey): The post on which the comment was made.
            content (TextField): The textual content of the comment.
            created_at (DateTimeField): Timestamp when the comment was created.
        Methods:
            __str__: Returns a string representation of the comment.
"""
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to="profiles/", blank=True, null=True)
    
    def __str__(self):
        return f"{self.user.username}'s profile"

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField(upload_to='posts/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    shared_post = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True)# self referential
    
    def __str__(self):
        return f"{self.user.username}'s post: {self.content[:20]}"

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('user', 'post')  # Prevent duplicate likes
    
    def __str__(self):
        return f"{self.user.username} liked {self.post}"

class Follow(models.Model):
    follower = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
    followed = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('follower', 'followed')  # Prevent duplicate follows
    
    def __str__(self):
        return f"{self.follower.username} follows {self.followed.username}"

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username}'s comment: {self.content[:20]}"