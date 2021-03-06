from django.contrib.auth.models import User
from django.db import models
from django.template.defaulttags import register
from django.utils.timezone import now
import re


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
    total_stocks = models.PositiveIntegerField()
    sold_stocks = models.IntegerField(default=0)
    price_per_stock = models.PositiveIntegerField()
    youtube_video_id = models.CharField(null=True, blank=True, max_length=50)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Uncomment if you don't want the slug to change every time the name changes
        if len(self.youtube_video_id) > 11:
            result = re.match('^[^v]+v=(.{11}).*', self.youtube_video_id)
            youtube = result.group(1)
            self.youtube_video_id = youtube
        super(Pitch, self).save(*args, **kwargs)

    @property
    def percentage_sold(self):
        return (self.sold_stocks * 100) / self.total_stocks

    @property
    def stocks_left(self):
        return self.total_stocks - self.sold_stocks

    @property
    def invested(self):
        invested = 0
        offers = Offer.objects.filter(pitch=self)
        for offer in offers:
            if offer.status == Offer.ACCEPTED:
                invested += (offer.price * offer.stock_count)

        return invested


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
    stock_count = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    seen = models.BooleanField(default=False)

    def __unicode__(self):
        return unicode("Offer: from '" + self.investor.user.username + "' for '" + self.pitch.title + "'")
