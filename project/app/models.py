from django.db import models


class UserProfile(models.Model):

    nick = models.CharField(max_length=30)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.nick


class Post(models.Model):

    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return 'Post'
