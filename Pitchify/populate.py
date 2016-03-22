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

        total_stocks = 400
        sold_stocks = 50  # TODO: verify
        pitches.append(self.add_pitch(
            companies[0],
            title="ISEE-3 Reboot Project",
            description="Our plan is simple: we intend to contact the ISEE-3 (International Sun-Earth Explorer) spacecraft, command it to fire its engines and enter an orbit near Earth, and then resume its original mission - a mission it began in 1978. ISEE-3 was rechristened as the International Comet Explorer (ICE). If we are successful it may also still be able to chase yet another comet. Working in collaboration with NASA we have assembled a team of engineers, programmers, and scientists - and have a large radio telescope fully capable of contacting ISEE-3.  If we are successful we intend to facilitate the sharing and interpretation of all of the new data ISEE-3 sends back via crowd sourcing. NASA has told us officially that there is no funding available to support an ISEE-3 effort - nor is this work a formal priority for the agency right now. But NASA does feel that the data that ISEE-3 could generate would have real value and that a crowd funded effort such as ours has real value as an education and public outreach activity. Time is short. And this project is not without significant risks.  We need your financial help. ISEE-3 must be contacted in the next month or so and it must complete its orbit change maneuvers no later than mid-June 2014. There is excitement ahead as well: part of the maneuvers will include a flyby of the Moon at an altitude of less than 50 km. Our team members at Morehead State University, working with AMSAT-DL in Germany, have already detected the carrier signals from both of ISEE-3's transmitters.  When the time comes, we will be using the large dish at Morehead State University to contact the spacecraft and give it commands. In order to interact with the spacecraft we will need to locate the original commands and then develop a software recreation of the original hardware that was used to communicate with the spacecraft. These are our two greatest challenges. The funding we seek will be used for things we have not already obtained from volunteers. We need to initiate a crash course effort to use 'software radio' to recreate virtual versions all of the original communications hardware that no longer physically exists. We also need to cover overhead involved in operating a large dish antenna, locating and analyzing old documentation, and possibly some travel. This activity will be led by the same team that has successfully accomplished the Lunar Orbiter Image Recovery Project (LOIRP) SkyCorp and SpaceRef Interactive.  Education and public outreach will be coordinated by the newly-formed non-profit organization Space College Foundation.  Our trajectory efforts will be coordinated by trajectory maestro Robert Farquhar and his team at KinetX.  We are also working in collaboration with the Science Mission Directorate at NASA Headquarters, NASA Goddard Spaceflight Center, and the Solar System Exploration Research Virtual Institute (SSERVI) at NASA Ames Research Center.",
            youtube_video_id='_AtVPGgA7BQ',
            total_stocks=total_stocks,
            sold_stocks=sold_stocks,
            price_per_stock=500
        ))

        total_stocks = 500
        sold_stocks = 70  # TODO: verify
        pitches.append(self.add_pitch(
            companies[1],
            title="Wavespring running shoes",
            description="My name is Andy Krafsur and I am obsessed about making shoes and helping people’s feet (and lives) be more comfortable.  As the Duck Dynasty patriarch Phil Robertson states in his new bestselling book, “Always wear shoes (your feet will feel better).”  We can all use a good pair of shoes as we travel on the roads through life! What do a spring and a duck call have in common? The Robertson's built a better duck call based upon their passion for hunting, and we believe we have built a better shoe based on our passion for running. Just as Phil Robertson denied the NFL to pursue his dream, I left a successful law practice to start Spira® with my wife, Holly. Like all entrepreneurial journeys, ours has been long and challenging, with a lot of ups and downs. But we continue to believe in the dream and are so excited to have this opportunity to bring these special shoes to you. We are offering several limited edition versions of the Duck Dynasty camouflage shoe available ONLY through this crowd funding project.  These remarkably comfortable shoes are based on our popular Spira® Stinger XLT performance shoe, which contains three WaveSprings--two in the forefoot and one in the heel. The shoes are lightweight (weigh only 8.4 ounces in a women's size 7 and 9.4 ounces in a men's size 9). For runners and non-runners alike, these shoes are one of only a handful of products available in the market with the distinctive Duck Dynasty camouflage pattern. So what is so great about springs and Spira® shoes that encouraged me to leave behind the practice of law and start a shoe company? I love running and had been searching for a shoe that could help make my runs more enjoyable, comfortable and productive.  Out of this pursuit, I tried many shoes and different footwear technologies, but none of the others compared to the WaveSpring®. ",
            youtube_video_id='clulwZnC1RA',
            total_stocks=total_stocks,
            sold_stocks=sold_stocks,
            price_per_stock=100
        ))

        total_stocks = 1000
        sold_stocks = 100  # TODO: verify
        pitches.append(self.add_pitch(
            companies[1],
            title="Extra Credits",
            description="Over the last year we've built up a web series talking about game design and the positive impact that games can have on humanity. We've used it to get people looking more deeply at videogames and thinking about what they can take away from their games and add to their lives. Yesterday Allison, our artist, found out she needed major shoulder surgery if she's going to be able to continue to do art.  Each show costs us far more than we make off of it; we've spent most of our reserves building Extra Credits and are now trying to give what we can to help Allison cover the cost of her surgery.  We need to raise somewhere between $15,000-$20,000 to help her get surgery and hire guest artists for the next few months, otherwise we can't keep doing the show. Help us fix the tiny pink bean so she can keep chasing us with a pencil...and please, please help us save Extra Credits. (If you donate, you will recieve all the rewards up through the level you donated at, so don't worry, if you donate $100 you'll recieve access to the episode, a tee-shirt, a publisher's club membership &c) ************ This has been more successful than our we could have possibly immagined.  We'd like to  take the overflow and pay it forward by creating jobs that allow other people to pursue their dreams...and, with luck and dedication, maybe make a real impact on the industry at the same time.",
            youtube_video_id='rN0qRKjfX3s',
            total_stocks=total_stocks,
            sold_stocks=sold_stocks,
            price_per_stock=300
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
