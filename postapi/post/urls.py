from django.urls import path
from .views import PostCreateListRetrieve, LikeAddRemove

urlpatterns = [
     path('', PostCreateListRetrieve.as_view(), name = 'post_list'), 
    path('<int:pk>/', PostCreateListRetrieve.as_view(), name = 'post_retrieve'),
    path('create/', PostCreateListRetrieve.as_view(), name = 'post_create'),
    path('like/<int:post_id>/', LikeAddRemove.as_view(), name = 'add_like'),
    
]