from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import RequestFactory
from django.test.client import Client

from pitchify import views
from pitchify.models import *


def add_pitch(pitch_title, pitch_description, youtubevideo):
    username = description = 'test'
    user = User()
    user.username = username
    user.password = username
    user.save()

    company = Company()
    company.user = user
    company.description = description
    company.save()

    pitch = Pitch()
    pitch.company = company
    pitch.price_per_stock = 10
    pitch.description = pitch_description
    pitch.total_stocks = 100
    pitch.title = pitch_title
    pitch.youtube_video_id = youtubevideo
    pitch.save()
    return pitch


#
# class CompanyMethodTest(TestCase):
#     def test_index_view_with_categories(self):
#         add_pitch('title 1', 'description 1')
#         add_pitch('title 2', 'description 2')
#         add_pitch('title 3', 'description 3')
#         add_pitch('title 4', 'description 4')
#
#         response = self.client.get(reverse('index'))
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, "title 4")
#
#         num_cats = len(response.context['pitches'])
#         self.assertEqual(num_cats, 4)

class IndexViewTests(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()

    def test_index_view(self):
        client = Client()
        response = client.get('/pitchify/')
        request = response.wsgi_request

        # request = self.factory.get('/pitchify/')
        response = views.index(request)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Pitchify helps you connect and share with the people in your life.")

class PitchTests(TestCase):
    def test_youtube_index(self):
        add_pitch('title 1', 'description 1', 'https://www.youtube.com/watch?v=9VoNgLnjzVg')
        pitch = Pitch.objects.get(title='title 1')
        self.assertEqual(pitch.youtube_video_id, '9VoNgLnjzVg')
    def test_youtube_edit(self):
        add_pitch('title 1', 'description 1', 'https://www.youtube.com/watch?v=9VoNgLnjzVg')
        pitch = Pitch.objects.get(title='title 1')
        pitch.youtube_video_id = 'https://www.youtube.com/watch?v=ZX8ZuMmaHIY'
        pitch.save()
        self.assertEqual(pitch.youtube_video_id, 'ZX8ZuMmaHIY')

