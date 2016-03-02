from datetime import datetime
from pprint import pprint

from Pitchify.models import Company, Investor, Pitch
from django.contrib.auth.models import User


class Population():
    def __init__(self):
        pass

    def populate(self, truncate=False):
        if (truncate):
            self.truncate()

        companies = self.add_companies()
        investors = self.add_investors()
        pitches = self.add_pitches(companies)

        # todo: offers
        return {
            'companies': companies,
            'investors': investors,
            'pitches': pitches
        }

    def add_companies(self):
        return [self.add_company("companyUser1", "some company description1"),
                self.add_company("companyUser2", "some company description2")]

    def add_investors(self):
        return [self.add_investor("investorUser1"),
                self.add_investor("investorUser2")]

    def add_pitches(self, companies):
        pitches = []
        i = 0
        for company in companies:
            i += 1
            pitches.append(self.add_pitch(
                company,
                title="My awesome pitch number " + i,
                description="just a very long description here for some random keywords for testing I believe this should do but is too long for a one liner so that might be a problem in code but who cares I definitely don't as you can see about this PEP8 guideline thing because they are only guidelines after all and I don't want to put hardcoded strings across many lines just to comply with the guidelines",
                youtube_video_id='6p1ypESj6nI',
                amount_required=10000,
                total_stocks=150,
                price_per_stock=100
            ))
        return pitches

    @staticmethod
    def add_company(username, description):
        user, created = User.objects.get_or_create(username=username)
        user.username = username
        user.save()

        company, created = Company.objects.get_or_create(user=user)
        company.user = user
        company.description = description

        company.save()
        return company

    @staticmethod
    def add_investor(username, website_url="", picture=""):
        user, created = User.objects.get_or_create(username=username)  # TODO: no idea, how to handle images
        user.username = username
        user.save()

        investor, created = Investor.objects.get_or_create(user=user)
        investor.user = user
        investor.website = website_url
        investor.picture = picture

    @staticmethod
    def add_pitch(company, title, description, amount_required, total_stocks, price_per_stock, youtube_video_id='', created=datetime.now()):
        pitch, created = Pitch.objects.get_or_create(company=company, title=title)
        pitch.description = description
        pitch.amount_required = amount_required
        pitch.total_stocks = total_stocks
        pitch.price_per_stock = price_per_stock
        pitch.youtube_video_id = youtube_video_id
        pitch.created = created
        pitch.save()
        return pitch

    def truncate(self):
        User.objects.all().delete()  # foreign keys clean objects in all other tables