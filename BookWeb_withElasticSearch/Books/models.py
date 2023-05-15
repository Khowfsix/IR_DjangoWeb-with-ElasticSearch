from django.db import models

# Create your models here.
class Book(models.Model):
    Ten = models.CharField(255)
    MaSanPham = models.CharField(255)
    Gia = models.FloatField()
    