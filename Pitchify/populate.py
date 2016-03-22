from datetime import datetime
from pprint import pprint
from random import randint

from django.contrib.auth.views import password_change

from pitchify.models import Company, Investor, Pitch, Offer
from django.contrib.auth.models import User


class Population:
    def __init__(self):
        pass

    def populate(self, truncate=False):
        if truncate:
            self.truncate()

        companies = self.add_companies()
        investors = self.add_investors()
        pitches = self.add_pitches(companies)
        offers = self.add_offers(investors, pitches)

        return {
            'companies': companies,
            'investors': investors,
            'pitches': pitches,
            'offers': offers,
        }

    def add_offers(self, investors, pitches):
        offers = []
        for pitch in pitches:
            for investor in investors:
                offers.append(self.add_offer(
                    pitch,
                    investor,
                    status=Offer.PENDING,
                    stock_count=10,
                    price=10,
                    message="Looking to buy stocks for the specified price", ))

                offers.append(self.add_offer(
                    pitch,
                    investor,
                    status=Offer.ACCEPTED,
                    stock_count=10,
                    price=10,
                    message="Looking to buy stocks for the specified price",
                    answer="Deal, we want this!",
                    seen=True, ))

                offers.append(self.add_offer(
                    pitch,
                    investor,
                    status=Offer.DECLINED,
                    stock_count=10,
                    price=5,
                    message="Looking to buy stocks for the specified price",
                    answer="Sorry, no lowballing!",
                    seen=True, ))

        return offers

    def add_companies(self):
        return [self.add_company("david", "David is the world's largest freelancing, outsourcing and crowdsourcing marketplace by number of users and projects. We connect over 18,585,760 employers and freelancers globally from over 247 countries, regions and territories. Through our marketplace, employers can hire freelancers to do work in areas such as software development, writing, data entry and design right through to engineering, the sciences, sales and marketing, accounting and legal services."),
                self.add_company("StudyPauseLtd", "Do you know what is going on in your university? Are you unsure which club to join? Having some spare time and want to do something interesting such as attending the social event of the month, networking with a CEO, or simply do some dances? Studypause is a consolidated image-display platform displaying UK university events - fast and easy-to-use, intuitive, and available on all devices. Events are chronologically ordered and can be filtered by categories. All the information you need is there - date and time, location, organising club, and event description. The application is not only an eco-friendly solution, but also improves the overall educational experience of thousands of students and helps them stay connected with each other and their institutions. Never miss out! Time to studypause!")]

    def add_investors(self):
        return [self.add_investor("leifos"),
                self.add_investor("laura")]

    def add_pitches(self, companies):
        pitches = []
        for company in companies:
            for i in range(1, 3):  # 2 pitches per company
                total_stocks = randint(100, 200)
                sold_stocks = randint(10, 100)
                pitches.append(self.add_pitch(
                    company,
                    title="My awesome pitch number " + str(i),
                    description="just a very long description here for some random keywords for testing I believe this should do but is too long for a one liner so that might be a problem in code but who cares I definitely don't as you can see about this PEP8 guideline thing because they are only guidelines after all and I don't want to put hardcoded strings across many lines just to comply with the guidelines",
                    youtube_video_id='6p1ypESj6nI',
                    total_stocks=total_stocks,
                    sold_stocks=sold_stocks,
                    price_per_stock=100
                ))
        return pitches

    def add_company(self, username, description):
        user, created = User.objects.get_or_create(username=username)
        user.set_password(username)
        user.username = username
        user.email = username + '@' + username + '.com'
        user.save()

        company, created = Company.objects.get_or_create(user=user)
        company.user = user
        company.description = description

        company.save()
        return company

    def add_investor(self, username, picture=""):
        user, created = User.objects.get_or_create(username=username)
        user.set_password(username)
        user.username = username
        user.email = username + '@' + username + '.com'
        user.save()

        investor, created = Investor.objects.get_or_create(user=user)
        investor.user = user
        investor.website = 'http://www.' + username + '.com'
        investor.picture = picture
        investor.save()

        return investor

    def add_pitch(self, company, title, description, total_stocks, sold_stocks, price_per_stock,
                  youtube_video_id='', created=datetime.now()):
        pitch, created = Pitch.objects.get_or_create(
            company=company,
            title=title,
            total_stocks=total_stocks,
            sold_stocks=sold_stocks,
            price_per_stock=price_per_stock,
            created=created)
        pitch.description = description
        pitch.youtube_video_id = youtube_video_id
        pitch.save()
        return pitch

    def add_offer(self, pitch, investor, status, stock_count, price, seen=False, message='', answer=''):
        offer, created = Offer.objects.get_or_create(
            pitch=pitch,
            investor=investor,
            status=status,
            stock_count=stock_count,
            price=price,
            seen=seen,
            answer=answer,
            message=message, )

        return offer

    def truncate(self):
        User.objects.all().delete()  # foreign keys clean objects in all other tables
