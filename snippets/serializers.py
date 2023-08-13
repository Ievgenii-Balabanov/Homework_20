from django.contrib.auth.models import User

from rest_framework import serializers

from snippets.models import Comment, Post


class PostSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    comments = serializers.HyperlinkedRelatedField(
        many=True, view_name="comment-detail", queryset=Post.objects.first().comments
    )

    class Meta:
        model = Post
        fields = ["url", "id", "owner", "title", "summary", "content", "created_on", "comments"]


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    post = serializers.HyperlinkedRelatedField(many=False, view_name="post-detail", queryset=Post.objects.all())

    class Meta:
        model = Comment
        fields = ["url", "id", "owner", "title", "body", "post", "created_on"]


class UserSerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.HyperlinkedRelatedField(many=True, view_name="post-detail", read_only=True)
    comments = serializers.HyperlinkedRelatedField(many=True, view_name="comment-detail", read_only=True)

    class Meta:
        model = User
        fields = ["url", "id", "username", "posts", "comments"]
