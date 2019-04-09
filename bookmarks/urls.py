from django.urls import path
from bookmarks import views as bookmarks_views
from django.views.generic.base import TemplateView
from .views import ListBookmarksView


urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('bookmark_list/', bookmarks_views.bookmark_list, name='bookmark_list'),
    path('user/<username>/', bookmarks_views.bookmark_user, name='bookmark_user'),
    path('bookmark/create/', bookmarks_views.bookmark_create, name='bookmark_create'),
    path('edit/<pk>/', bookmarks_views.bookmark_edit, name='bookmark_edit'),
    
    path('bookmarks/', ListBookmarksView.as_view(), name="bookmarks-all"),
]