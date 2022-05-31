from django.db import models
from account.models import CustomUser
from main.models import Song


class Order(models.Model):
    user = models.ForeignKey(CustomUser, related_name='user', on_delete=models.CASCADE)
    song = models.ForeignKey(Song, related_name='product', on_delete=models.DO_NOTHING,)
    count = models.IntegerField()