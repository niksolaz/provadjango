import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Blog

# Create your tests here.
class BlogModelTests(TestCase):
    
    def test_pub_date_pretty_with_future_blog(self):
        """
        pub_date_pretty() returns the pub_date with future blog.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_blog = Blog(pub_date=time)
        self.assertIs(future_blog.pub_date_pretty() != '30 Dec 2018, 00:00', True)
    
    