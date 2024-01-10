from django.shortcuts import render
from .models import post
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

class PostListView(ListView):
    model = post
    template_name = 'forum.html' 
    context_object_name = 'posts'
    ordering = ['-creation_date']

class PostDetailView(DetailView):
    template_name='post_detail.html'
    model = post


class PostCreateView( CreateView):
    template_name='post_upload.html'
    model = post
    fields = ['author','title', 'description','writing_language','additional_information','contact']

    def form_valid(self, form):
        return super().form_valid(form)

# Create your views here.
"""
def forum(request):

    context = {
        'posts': post
    }
    return render(request, "forum.html",context)
"""