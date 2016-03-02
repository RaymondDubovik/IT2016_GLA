from pprint import pprint

from Pitchify.models import Company, Investor
from django.contrib.auth.models import User


class Population():
    def __init__(self):
        pass

    def populate(self, truncate=False):
        if (truncate):
            self.truncate()

        companies = self.add_companies()
        investors = self.add_investors()

        # todo: stuff;
        return {
            'companies': companies,
            'investors': investors,
        }

    def add_companies(self):
        return [self.add_company("companyUser1", "some company description1"),
                self.add_company("companyUser2", "some company description2")]

    def add_investors(self):
        return [self.add_investor("investorUser1"),
                self.add_investor("investorUser2")]

    def add_company(self, username, description):
        user, created = User.objects.get_or_create(username=username)
        user.username = username
        user.save()

        company, created = Company.objects.get_or_create(user=user)
        company.user = user
        company.description = description

        company.save()
        return company

    def add_investor(self, username, website_url="", picture=""):
        user, created = User.objects.get_or_create(username=username)  # TODO: no idea, how to handle images
        user.username = username
        user.save()

        investor, created = Investor.objects.get_or_create(user=user)
        investor.user = user
        investor.website = website_url
        investor.picture = picture

    def truncate(self):
        User.objects.all().delete()  # foreign keys clean objects in all other tables
