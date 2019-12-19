from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    headline = models.CharField(max_length=70)
    content = models.TextField()
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.headline


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.content[0:40]}...'
