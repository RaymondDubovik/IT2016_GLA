from django.contrib.auth.models import User
from django.db import models


class Company(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    description = models.TextField(blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username


class Investor(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username


class Pitch(models.Model): # foreign company
    company_id = models.ForeignKey(Company)
    title = models.CharField(max_length=100)
    description = models.TextField()
    youtube_video_id = models.CharField(max_length=11)
    amount_required = models.IntegerField()
    created = models.DateTimeField()
    total_stocks = models.IntegerField()
    price_per_stock = models.IntegerField()

class Offer(models.Model):
    PENDING = 'P'
    ACCEPTED = 'A'
    DECLINED = 'D'

    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (ACCEPTED, 'Accepted'),
        (DECLINED, 'Declined'),
    ]

    pitch_id = models.ForeignKey(Pitch)
    investor_id = models.ForeignKey(Investor)
    status = models.CharField(max_length=1) # TODO: implement choices
    message = models.TextField()
    answer = models.TextField()
    stock_count = models.IntegerField()
    price = models.IntegerField()
    seen = models.BooleanField(default=False)


