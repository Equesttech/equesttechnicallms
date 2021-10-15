from . import views
from django.urls import path
from django.urls import include



app_name = 'blog'

urlpatterns = [
    path('', views.PostList.as_view(), name='bloghome'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]
