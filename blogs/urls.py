from django.urls import path
from . import views

urlpatterns = [
    path("view_blogs/", views.blogs, name="view_blogs"),
    path("add_post/", views.add_post, name="add_post"),
    path('update_post/<int:post_id>/', views.update_post, name="update_post"),
    path('delete_post/<int:post_id>/', views.delete_post, name="delete_post"),
]
