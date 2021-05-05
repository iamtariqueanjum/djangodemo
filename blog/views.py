from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Article
from .forms import ArticleModelForm

from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)
# Create your views here.

class ArticleCreateView(CreateView):
    form_class = ArticleModelForm
    template_name = 'blog/article_create.html'
    queryset = Article.objects.all()

    def form_valid(self, form):
        # print(form.cleaned_data)
        return super().form_valid(form)

    # def get_success_url(self):
    #     return '/'

class ArticleUpdateView(UpdateView):
    form_class = ArticleModelForm
    template_name = 'blog/article_create.html'
    queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Article, id=id_)

    def form_valid(self, form):
        # print(form.cleaned_data)
        return super().form_valid(form)

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

class ArticleDeleteView(DeleteView):
    # queryset = Article.objects.filter(id__gt=1) # filters the queryset greater than
    queryset = Article.objects.all()

    #success_url = '../../'

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Article, id=id_)

    def get_success_url(self):
        return reverse('blog:article-list')
