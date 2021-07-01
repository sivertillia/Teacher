from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    body = models.TextField(blank=True, db_index=True)
    date_pub = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=100, unique=True)