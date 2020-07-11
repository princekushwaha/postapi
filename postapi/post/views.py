from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView, CreateAPIView, DestroyAPIView
from .serializers import PostSerializer, LikeSerializer
from .models import Post, Likes
from rest_framework.response import Response
from rest_framework import status, permissions, authentication
from rest_framework.serializers import ListSerializer

# Create your views here.

class PostCreateListRetrieve(CreateAPIView, ListAPIView, RetrieveAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author = self.request.user)



class LikeAddRemove(CreateAPIView, DestroyAPIView):

    serializer_class = LikeSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    lookup_url_kwargs = 'post_id'

    def create(self, request, *args, **kwargs):
        user = self.request.user
        post  = Post.objects.get(id =  self.kwargs.get(self.lookup_url_kwargs))
        data = {'liked_by' : user, 'post' : post}
        
        if Likes.objects.filter(liked_by = user, post = post).exists():
            return Response(data = {'message' : 'You Already Liked'}, status=status.HTTP_208_ALREADY_REPORTED)
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer, data)
        headers = self.get_success_headers(serializer.data)
        return Response(data = {'message' : 'Succesfully Liked'}, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer, data):
        serializer.save(liked_by = data['liked_by'], post = data['post'])

    def get_object(self):
       
        user = self.request.user 
        post  = Post.objects.get(id =  self.kwargs.get(self.lookup_url_kwargs))
        instance = Likes.objects.filter(liked_by = user, post = post)
        return instance
    
    def destroy(self, request, *args, **kwargs):

        instance = self.get_object()
       
        if instance.__len__() == 0:
          return Response(data = {'message' : 'Not Liked Yet', },status=status.HTTP_204_NO_CONTENT)
        self.perform_destroy(instance)
        return Response(data = {'message' : 'Like Deleted', },status=status.HTTP_204_NO_CONTENT)

    


        
    
   



