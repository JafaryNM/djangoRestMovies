from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

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
    platform=models.ForeignKey(StreamPlatform,models.CASCADE, related_name='watchlist')
    avg_rating=models.FloatField(default=0)
    number_rating=models.IntegerField(default=0)
    created=models.DateField()
    
    def __str__(self):
        return self.title

class Review(models.Model):
    review_user=models.ForeignKey(User, on_delete=models.CASCADE)
    review=models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    description=models.CharField(max_length=200, null=True)
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now=True)
    watchlist=models.ForeignKey(WatchList,models.CASCADE, related_name='reviews')
    active=models.BooleanField(default=True)
    
    def __str__(self):
        
        # Convert into string name
        
        return str(self.review) + " | "  + self.watchlist.title
    
    