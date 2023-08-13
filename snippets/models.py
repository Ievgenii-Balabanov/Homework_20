from django.db import models
from django.contrib import auth


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    summary = models.CharField(max_length=100)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey("auth.User", related_name="posts", on_delete=models.CASCADE)

    def __str__(self):
        return f"Post id: {self.id}, Title: {self.title}, Summary: {self.summary}"

    class Meta:
        ordering = ["created_on"]


class Comment(models.Model):
    title = models.CharField(max_length=200, unique=True)
    body = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    owner = models.ForeignKey("auth.User", related_name="comments", on_delete=models.CASCADE)

    def __str__(self):
        return f"Comment id: {self.id}, Title: {self.title}, Summary: {self.body}"

    class Meta:
        ordering = ["created_on"]
