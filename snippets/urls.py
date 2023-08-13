# from django.urls import path
#
# from rest_framework.urlpatterns import format_suffix_patterns
#
# from snippets.views import PostViewSet, UserViewSet, api_root, CommentViewSet
#
# post_list = PostViewSet.as_view({"get": "list", "post": "create"})
# post_detail = PostViewSet.as_view(
#     {
#         "get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"
#     }
# )
# comment_list = CommentViewSet.as_view({"get": "list", "post": "create"})
# comment_detail = CommentViewSet.as_view(
#     {
#         "get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"
#     }
# )

# user_list = UserViewSet.as_view({"get": "list"})
# user_detail = UserViewSet.as_view({"get": "retrieve"})
#
# urlpatterns = format_suffix_patterns([
#     path("", api_root),
#
#     path("posts/", post_list, name="post-list"),
#     path("posts/<int:pk>/", post_detail, name="post-detail"),
#
#     path("comments/", comment_list, name="comment-list"),
#     path("posts/<int:pk>/comments/", comment_detail, name="comment-detail"),
#
#     path("users/", user_list, name="user-list"),
#     path("users/<int:pk>/", user_detail, name="user-detail")
# ])


from django.urls import path, include

from rest_framework.routers import DefaultRouter

from snippets import views

router = DefaultRouter()
router.register(r"Posts", views.PostViewSet, basename="post")
router.register(r"Comments", views.CommentViewSet, basename="comment")
router.register(r"Users", views.UserViewSet, basename="user")

urlpatterns = [
    path("", include(router.urls)),
]
