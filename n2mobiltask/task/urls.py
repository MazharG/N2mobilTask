from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsersViewSet, AlbumsViewSet, PhotosViewSet, PostsViewSet, CommentsViewSet, TodosViewSet

router = DefaultRouter()
router.register(r'users', UsersViewSet)
router.register(r'albums', AlbumsViewSet)
router.register(r'photos', PhotosViewSet)
router.register(r'posts', PostsViewSet)
router.register(r'comments', CommentsViewSet)
router.register(r'todos', TodosViewSet)

urlpatterns = [
    path('', include(router.urls)),
]