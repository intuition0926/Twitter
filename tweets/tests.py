from django.test import TestCase
from django.contrib.auth.models import User
from tweets.models import Tweet
from datetime import timedelta
from utils.timer_helper import utc_now

# Create your tests here.

class TweetTest(TestCase):

    def test_hours_to_now(self):
        laofuzi = User.objects.create_user(username='laofuzi')
        tweet = Tweet.objects.create(user=laofuzi, content='first tweet project')
        tweet.created_at = utc_now() - timedelta(hours=10)
        tweet.save()
        self.assertEqual(tweet.hours_to_now, 10)
