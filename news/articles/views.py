from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import UpdateView,DeleteView, CreateView 
from .models import Articles
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied 

class ArticleListView(ListView):
    model = Articles
    template_name = 'article_list.html'
    
class ArticleDetailView(LoginRequiredMixin,DetailView):
    model = Articles
    login_url = 'login'
    template_name = 'article_detail.html'
    
class ArticleUpdateView(LoginRequiredMixin,UpdateView):
    model = Articles
    fields = ('title','body',)
    template_name = 'article_edit.html'
    login_url = 'login'
    success_url = reverse_lazy('article_list')
    def dispatch(self, request, *args, **kwargs): # new
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class ArticleDeleteView(LoginRequiredMixin,DeleteView):
    model = Articles
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
    login_url = 'login'
    def dispatch(self, request, *args, **kwargs): # new
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
class ArticleCreateView(LoginRequiredMixin,CreateView):
    model = Articles
    template_name = 'article_new.html'
    fields = ('title', 'body',)
    success_url = reverse_lazy('article_list')
    login_url = 'login'
    def form_valid(self, form) -> HttpResponse:
        form.instance.author = self.request.user
        return super().form_valid(form)