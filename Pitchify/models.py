from django.contrib.auth.models import User
from django.db import models
from django.template.defaulttags import register
from django.utils.timezone import now

class Company(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    description = models.TextField(blank=True)

    def __unicode__(self):
        return self.user.username


class Investor(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __unicode__(self):
        return self.user.username


class Pitch(models.Model):  # foreign company
    company = models.ForeignKey(Company)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, default=now)
    total_stocks = models.IntegerField()
    sold_stocks = models.IntegerField(default=0)
    price_per_stock = models.IntegerField()
    youtube_video_id = models.CharField(null=True, blank=True, max_length=50)

    def __unicode__(self):
        return self.title

    @property
    def percentage_sold(self):
        return (self.sold_stocks * 100)/self.total_stocks

    @property
    def stocks_left(self):
        return self.total_stocks - self.sold_stocks

    @property
    def invested(self):
        return self.sold_stocks * self.price_per_stock


class Offer(models.Model):
    PENDING = '?'
    ACCEPTED = 'A'
    DECLINED = 'D'

    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (ACCEPTED, 'Accepted'),
        (DECLINED, 'Declined'),
    ]

    pitch = models.ForeignKey(Pitch)
    investor = models.ForeignKey(Investor)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=PENDING)
    message = models.TextField(null=True, blank=True)
    answer = models.TextField(null=True, blank=True)
    stock_count = models.IntegerField()
    price = models.IntegerField()
    seen = models.BooleanField(default=False)

    def __unicode__(self):
        return unicode("Offer: from '" + self.investor.user.username + "' for '" + self.pitch.title + "'")
