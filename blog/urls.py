from django.urls import path
from . import views             # . means current directory
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView

urlpatterns = [
    # path('', views.home, name='blog-home'),               # since we entered /blog on the website it will be chopped off by include and the rest will be passed to blog.urls, which is an empty string and we will get 'Blog Home'
    path('', PostListView.as_view(), name='blog-home'),     # since we entered /blog on the website it will be chopped off by include and the rest will be passed to blog.urls, which is an empty string and we will get 'Blog Home'
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),           # <int:pk> is a primary key, pk is the primary key of the post we want to view
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),     # <str:username> is a string, username is the username of the user whose posts we want to view
    path('about/', views.about, name='blog-about'),
]

# Convention for template name of PostListView <app>/<model>_<viewtype>.html
# Convention name of PostDetailView post-detail.html
# Convention name of PostCreateView name-of-model_form.html
# Convention name of PostUpdateView name-of-model_form.html
# Convention name of PostDeleteView name-of-model_confirm_delete.html
# path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail') here we passed a variable in urlpatterns