from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
from datetime import date
from commerce import settings
#from django.contrib.auth.models import User 


class User(AbstractUser):
    pass

class Auctions(models.Model):
    CATEGORIES = (
    ('LAP', 'Laptop'),
    ('CTH', 'Clothing'),
    ('PRO', 'Properties'),
    ('Cat', 'No Category selected')
    )
    Title = models.CharField(max_length=100)
    Body = models.TextField()
    Creator = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    Image = models.ImageField(upload_to ="images/")
    pub_date = models.DateTimeField( auto_now_add=True,null=True, blank=True)
    Price = models.DecimalField(max_digits=50, decimal_places=2)
    category = models.CharField(null=True, blank=True,
    max_length=10,
    choices=CATEGORIES
    )

    def __str__(self):
        return self.Title
    
    def summary(self):
        return self.Body[:100]

    def get_absolute_url(self):
        """Returns the url to access a detail record for this auction."""
        return reverse('list-detail', args=[str(self.id)]) 

    @property
    def image_url(self):
        if self.Image and hasattr(self.Image, 'url'):
            return self.Image_url   


class Bids(models.Model):
    user_id = models.ForeignKey(User, default= "", on_delete=models.CASCADE,null=True, blank=True)
    auction_id = models.ForeignKey(Auctions, default= "", on_delete=models.CASCADE,null=True, blank=True)
    value = models.PositiveIntegerField(null=True, blank=True)
    

class Comment(models.Model):
    user_id = models.ForeignKey(User, default= "", on_delete=models.CASCADE)
    comment = models.TextField()


class Watchlist(models.Model):
   user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
   item = models.ManyToManyField(Auctions)
   def __str__(self):
       return f"{self.user}'s WatchList"