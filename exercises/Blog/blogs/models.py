from django.db import models
from django.contrib.auth.models import User


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()

    class Meta:
        verbose_name_plural = 'posts'

    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()

    class Meta:
        verbose_name_plural = 'comments'

    def __str__(self) -> str:
        if len(self.comment) > 50:
            return self.comment[:50]+"..."
        else:
            return self.comment
