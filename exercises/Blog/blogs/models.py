from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    class Meta:
        verbose_name_plural = 'posts'

    def __str__(self) -> str:
        return self.title
