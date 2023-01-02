from django.db import models

# Create your models here.
class Likes(models.Model):
    num_of_likes = models.IntegerField()