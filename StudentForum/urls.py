from django.urls import path
from . import views
from .views import (
    PostListView,
    PostCreateView,
    PostDetailView

)

app_name = "studentforum"
urlpatterns = [
    path('', PostListView.as_view(), name='main'),
    path('<int:pk>/',PostDetailView.as_view(), name='post_view'),
    path('create/',PostCreateView.as_view(), name='create_view'),

]
