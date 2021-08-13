from django import forms
from django.db.models.fields import SlugField
from .models import Post, Tag
from django.core.exceptions import ValidationError
class TagForm(forms.Form):
    title = forms.CharField(max_length=50)
    slug = forms.CharField(max_length=50)

    title.widget.attrs.update({'class': 'form-control'})
    slug.widget.attrs.update({'class': 'form-control'})


    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()
        if new_slug == 'create':
            raise ValidationError('Slug may not be "create"')
        if Tag.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError('Er')
        return new_slug

    def save(self):
        # print('SAVE', self.slug)
        new_slug = Tag.objects.create(
            title = self.cleaned_data['title'],
            slug = self.cleaned_data['slug'])
        return new_slug