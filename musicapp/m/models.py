from django.db import models

# Create your models here.


class lag(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pic',blank=True)

class art_cat(models.Model):
    name = models.CharField(max_length=100)
    art_img = models.ImageField(upload_to='pic',blank=True)
    
    

class song_cat(models.Model):
    name = models.CharField(max_length=100)
    cat_img = models.ImageField(upload_to='pic',blank=True)
    
    
class song(models.Model):
    title = models.CharField(max_length=100)
    lag = models.ForeignKey(lag,on_delete=models.CASCADE,blank=True,null=True)
    art_cat = models.ForeignKey(art_cat,on_delete=models.CASCADE,blank=True,null=True)
    song_cat = models.ForeignKey(song_cat,on_delete=models.CASCADE,blank=True,null=True)
    m_name  = models.CharField(max_length=200)
    art = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pic')
    audio = models.FileField(upload_to='pic')
    