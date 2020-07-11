from django.db import models
from  accounts.models import UserModel
# Create your models here.


class Post(models.Model):

    author = models.ForeignKey(UserModel, on_delete = models.CASCADE)
    body = models.TextField()
    image = models.ImageField(upload_to = 'image', blank = True, null = True)
    uploaded_on = models.DateTimeField(auto_now_add = True)

    def get_like_url(self):

        return 'http://127.0.0.1:8000/post/like/' + str(self.id) + '/'

    def __str__(self):
        return self.body

    def get_fullname(self):
        return self.author.first_name
    
    def get_username(self):
        return self.author.username


class Likes(models.Model):

    liked_by = models.ForeignKey(UserModel, on_delete = models.DO_NOTHING)
    post = models.ForeignKey(Post, on_delete = models.CASCADE)

    class Meta:

        unique_together = ['liked_by', 'post']

    
    