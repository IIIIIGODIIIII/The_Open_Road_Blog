from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin    
from django.contrib.auth.models import User   
# LoginRequiredMixin is a class that we can add to our views to require that the user is logged in as decorators are not allowed for classes
# UserPassesTestMixin is a class that we can use so that the user who created the blog post can only edit it

# Create your views here.

# posts = [
#     {
#         'author': 'Aditya',
#         'title': 'Blog Post 1',
#         'content': 'First post content',
#         'date_posted': 'June 11, 2024'
#     },
#     {
#         'author': 'Chaitanya',
#         'title': 'Blog Post 2',
#         'content': 'Second post content',
#         'date_posted': 'June 14, 2024'
#     }
# ]

def home(request):
    context = {
        # 'posts': posts          # This is a dictionary, LHS is key and RHS is value, RHS is a list of dictionaries
          'posts': Post.objects.all()    
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

# View for displaying a list of posts
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'     # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']          # '-' sign is used to reverse the order of the posts
    paginate_by = 2                      # Number of posts per page

# View for displaying all the posts of a particular user
class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'     # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 2                            # Number of posts per page

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))      # Get the user with the username from the URL
        return Post.objects.filter(author=user).order_by('-date_posted')          # Get all the posts of the user and order them by date posted

# View for displaying information on a single post
class PostDetailView(DetailView):
    model = Post
           
# View for creating a new post
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# View for updating a post
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:        # If current user is the author of the post
            return True
        return False
    
# View for deleting a post
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'       # Redirect to home page after deleting a post

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:        # If current user is the author of the post
            return True
        return False