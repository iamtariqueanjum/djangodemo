from django.shortcuts import render, get_object_or_404

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

class ArticleDetailView(DetailView):
    #queryset = Article.objects.filter(id__gt=1) # filters the queryset greater than
    queryset = Article.objects.all()
    # to override pk with id
    # def get_object(self):
    #     id_ = self.kwargs.get("id")
    #     return get_object_or_404(Article, id=id_)