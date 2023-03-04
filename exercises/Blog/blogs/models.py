from django.db import models

# Create your models here.


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    entry = models.TextField()

    def __str__(self) -> str:
        return super().__str__()
