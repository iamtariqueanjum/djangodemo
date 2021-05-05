from django.shortcuts import render

from .models import Article

from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)
# Create your views here.

class ArticleListView(ListView):
    # template_name = 'blog/article_list.html' -- app_name/<model_name>_viewname.html
    queryset = Article.objects.all()