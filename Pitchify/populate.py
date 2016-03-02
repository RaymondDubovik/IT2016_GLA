from pprint import pprint

from Pitchify.models import Company
from django.contrib.auth.models import User


class Population():
    def __init__(self):
        pass

    def populate(self):
        return {
            'companies': self.add_companies(),
            'investors': self.add_investors(),
        }

    def add_companies(self):
        list = []
        list.append(self.add_company("testUser1", "some company description"))
        return list

    def add_investors(self):
        print ('adding investors')

    def add_company(self, username, description):
        user, created = User.objects.get_or_create(username=username)
        user.username = username
        user.save()

        company, created = Company.objects.get_or_create(user=user)
        company.user = user
        company.description = description

        company.save()
        return company

    def add_investor(self):
        print ('adding investor')

    '''
    python_cat = add_cat("Python", views=128, likes=64)

    add_page(cat=python_cat,
             title="Official Python Tutorial",
             url="http://docs.python.org/2/tutorial/")

    # Print out what we have added to the user.

    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print "- {0} - {1}".format(str(c), str(p))



def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url = url
    p.views = views
    p.save()
    return p


def add_cat(name, likes, views):
    c = Category.objects.get_or_create(name=name)[0]
    c.views = views
    c.likes = likes
    c.save()
    return c
'''
