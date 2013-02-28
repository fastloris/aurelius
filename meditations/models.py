from django.db import models

# Create your models here.

class BookSection(models.Model):
    book = models.IntegerField()
    section = models.IntegerField()
    content = models.TextField()
