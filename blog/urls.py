from django.urls import path

from .views import (
    ArticleCreateView,
    ArticleListView,
    ArticleDetailView,
    ArticleUpdateView,
    ArticleDeleteView
)

app_name = 'blog'
urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    path('create/', ArticleCreateView.as_view(), name='article-create'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    # path('<int:id>', ArticleDetailView.as_view(), name='article-detail'),
    path('<int:pk>/update/', ArticleUpdateView.as_view(), name='article-update'),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='article-delete'),
]
