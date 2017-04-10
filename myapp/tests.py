from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.core.urlresolvers import resolve, reverse
from . import views


class PageTest(TestCase):
    """ All pages should:
        1. resolve to the proper view
        2. return a 200 (login_required urls return  302 if not logged in
        3. use the appropriate template
        4. contain the proper
        """
    fixtures = []

    def test_home_page(self):
        """
        Test the home page

        """
        url = reverse('myapp:home')
        v = resolve(url)
        self.assertEqual(v.func.__name__, views.HomeView.__name__)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'myapp/home.html')

    def test_profile_page(self):
        """
        Test the about page

        """
        url = reverse('myapp:profile')
        v = resolve(url)
        self.assertEqual(v.func.__name__, views.ProfileView.__name__)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'myapp/profile.html')

    def test_people_page(self):
        """
        Test the about page

        """
        url = reverse('myapp:people')
        v = resolve(url)
        self.assertEqual(v.func.__name__, views.PeopleView.__name__)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'myapp/people.html')



