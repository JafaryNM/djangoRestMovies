from django.db import models

# Create your models here.

class StreamPlatform(models.Model):
    name=models.CharField(max_length=30)
    about=models.CharField(max_length=159)
    website=models.URLField(max_length=100)
    
    def __str__(self):
        return self.name

class WatchList(models.Model):
    title=models.CharField(max_length=100)
    storyline=models.TextField()
    active=models.BooleanField(default=True)
    platform=models.ForeignKey(StreamPlatform,models.CASCADE,related_name='watchlist')
    created=models.DateField()
    
    def __str__(self):
        return self.title
     
     