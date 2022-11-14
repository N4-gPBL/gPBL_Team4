from django.db import models

# Create your models here.

# Post

class Post(models.Model):
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)
    content = models.TextField(null=True,blank=True)
    summary = models.TextField(null=True,blank=True)
    categoryId = models.IntegerField()
    slug = models.TextField()
    title = models.TextField()

    class Meta:
        ordering = ["createdAt"]