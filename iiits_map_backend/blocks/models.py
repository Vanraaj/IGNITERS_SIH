from django.db import models

# Create your models here.
class Classroom(models.Model):
    room_no = models.CharField(max_length=3, default='NULL')
    images = models.ImageField(upload_to='images/', default='NULL')

class Office(models.Model):
    Name = models.CharField(max_length=30, default='NULL')
    images = models.ImageField(upload_to='images/', default='NULL')

class Miscellaneous(models.Model):
    images = models.ImageField(upload_to='images/', default='NULL')

class FacultyRoom(models.Model):
    Name = models.CharField(max_length=30, default='NULL')
    room_no = models.CharField(max_length=3, default='NULL')
    images = models.ImageField(upload_to='images/', default='NULL')
