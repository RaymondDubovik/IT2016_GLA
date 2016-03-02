from django.contrib.auth.models import User
from django.db import models


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
    amount_required = models.IntegerField()
    created = models.DateTimeField()
    total_stocks = models.IntegerField()
    price_per_stock = models.IntegerField()
    youtube_video_id = models.CharField(null=True, blank=True, max_length=11)

    def __unicode__(self):
        return self.title


class Offer(models.Model):
    PENDING = 'P'
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
    message = models.TextField()
    answer = models.TextField()
    stock_count = models.IntegerField()
    price = models.IntegerField()
    seen = models.BooleanField(default=False)

    def __unicode__(self):
        return "Offer: from '" + self.investor.user.username + "' for '" + self.pitch.title + "'"