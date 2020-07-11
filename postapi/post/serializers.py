from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from .models import Post, Likes
from rest_framework import serializers


class PostSerializer(ModelSerializer):
    liked = serializers.SerializerMethodField(read_only = True)
    like_url = serializers.URLField(source = 'get_like_url', read_only = True)
    total_likes = serializers.SerializerMethodField()
    author_fullname = serializers.CharField(read_only = True, source = 'get_fullname')
    author_username = serializers.CharField(read_only=True, source = 'get_username')
    
    class Meta:
        model = Post
        fields = ['author_fullname','author_username', 'body', 'image','uploaded_on', 'liked','total_likes', 'like_url']

        extra_kwargs = {
            'author' : {
                'read_only' : True, 
            }
        }

       
    
    def get_total_likes(self, obj):
        likes = Likes.objects.filter(post = obj)
        print((self.context.get('request')).parsers)  
        return likes.count()
    
    def get_liked(self, obj):
        likes = Likes.objects.filter(liked_by = self.context.get('request').user, post = obj)
        if likes.count() == 0:
            return "False"
        else:
            return "True"




class LikeSerializer(ModelSerializer):
    
    # post = serializers.SerializerMethodField()
    class Meta:
        model = Likes
        fields = ['liked_by', 'post']

        extra_kwargs = {
            'liked_by' : {
                'required' : 'False',
                'read_only' : True, 
            },
            'post' : {
                'required' : 'False',
                'read_only' : True,
            }
        }

    
        




