from time import time
from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify


def gen_slug(self):
    new_slug = slugify(self, allow_unicode=True)
    return new_slug + '-' + str(int(time))


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    body = models.TextField(blank=True, db_index=True)
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=100, unique=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')

    def get_absoluter_url(self):
        return reverse('post_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return '{}'.format(self.title)

    # def save(self, *args, **kwargs):
    #     if not self.id:
    #         self.slug = gen_slug(self.title)
    #     super().save(*args, **kwargs)


class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def get_absoluter_url(self):
        return reverse('tag_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return '{}'.format(self.title)
