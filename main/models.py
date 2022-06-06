from django.db import models

# Create your models here.
from account.models import CustomUser


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, primary_key=True)

    def __str__(self):
        return self.name


class Song(models.Model):
    name = models.CharField(max_length=100)
    singer = models.CharField(max_length=100)
    owner = models.ForeignKey(CustomUser, related_name='songs', on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(Category, related_name='songs', on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='images', null=True, blank=True)


    def __str__(self):
        return f'{self.name} - {self.singer}'

class Review(models.Model):
    owner = models.ForeignKey(CustomUser, related_name='reviews', on_delete=models.CASCADE)
    song = models.ForeignKey(Song, related_name='reviews', on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.owner} -> {self.song} -> {self.created_at}'



class Likes(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='liked')

    class Meta:
        unique_together = ['song', 'user']

