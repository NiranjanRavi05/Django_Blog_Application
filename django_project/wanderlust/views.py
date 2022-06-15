from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post

# Function to display the home page of the web application
def wanderlust_home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'wanderlust/home.html', context)

# Function to display the about page
def wanderlust_about(request):
    return render(request, 'wanderlust/about.html', {'title': 'Experience'})

# Class to display the blog posts in a list manner in the home page 
class PostListView(ListView):
    model = Post
    template_name = 'wanderlust/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 3

# Class to display the posts created by a specific user
class UserPostListView(ListView):
    model = Post
    template_name = 'wanderlust/user_posts.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

# Class to display the post in a detailed manner
class PostDetailView(DetailView):
    model = Post

#Class to display the creation page for the blog posts
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# Class to display the page where the user can edit/delete the blog post
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

# Class to display the confirmation of deletion of blog post
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = "/"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

