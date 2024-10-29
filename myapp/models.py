from django.db import models

# Create your models here.

class Home(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    images = models.ImageField(upload_to='images/')
    
class Access(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    
class About(models.Model):
    image = models.ImageField(upload_to='about/')
    
class About1(models.Model):
    image = models.ImageField(upload_to='about1/')
    name = models.CharField(max_length=200)
    description = models.TextField()
    
class Featue(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    
class Featue1(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    
class Featue2(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    
class Benefit(models.Model):
    image = models.ImageField(upload_to='benefit/')
    name = models.CharField(max_length=200)
    description = models.TextField()
    
class Bmi(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    description = models.TextField()
    
class Trainer(models.Model):
    image = models.ImageField(upload_to='benefit/')
    name = models.CharField(max_length=200)
    description = models.TextField()
    
class Client(models.Model):
    image = models.ImageField(upload_to='client/')
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.TextField()
    
class Blog(models.Model):
    image = models.ImageField(upload_to='blog/')
    name = models.CharField(max_length=200)
    description = models.TextField()
    url = models.URLField()
    
class Subscribe(models.Model):
    image = models.ImageField(upload_to='subscribe/')

