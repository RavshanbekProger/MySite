from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.safestring import mark_safe

# Create your models here.
class Setting(models.Model):
    title = models.CharField(max_length=255)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    company = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=255, blank=True)
    fax = models.CharField(max_length=255, blank=True)
    email = models.EmailField(max_length=255, blank=True)
    telegram = models.CharField(max_length=255, blank=True)
    instagram = models.CharField(max_length=255, blank=True)
    facebook = models.CharField(max_length=255, blank=True)
    youtube = models.CharField(max_length=255, blank=True)
    twitter = models.CharField(max_length=255, blank=True)
    aboutus = RichTextUploadingField(blank=True)
    contact = RichTextUploadingField(blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Post(models.Model):  # kompaniya yangiliklari
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    detail = RichTextUploadingField()
    image = models.ImageField(upload_to='media/images/')
    author = models.CharField(max_length=255, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50">'.format(self.image.url))

    image_tag.short_description = 'Image'

class ImagesPost(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True)
    image = models.ImageField(blank=True, upload_to='media/images/')

    def __str__(self):
        return self.title

class License(models.Model):  # kompaniya savdo sotiq huquqi hujjatlari
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    detail = RichTextUploadingField()
    image = models.ImageField(upload_to='media/images/')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50">'.format(self.image.url))

    image_tag.short_description = 'Image'

class ImagesLic(models.Model):
    license = models.ForeignKey(License, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True)
    image = models.ImageField(blank=True, upload_to='media/images/')

    def __str__(self):
        return self.title
