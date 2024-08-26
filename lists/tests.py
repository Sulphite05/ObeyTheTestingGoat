from django.test import TestCase
from django.http import HttpRequest
from lists.views import home_page

# Create your tests here.
class SmokeTest(TestCase):
    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode("utf-8")
        self.assertIn("<title>To-Do lists</title>", html)
        self.assertTrue(html.startswith("<html>"))
        self.assertTrue(html.endswith("</html>"))


# Django is structured along a classic Model-View-Controller (MVC) pattern.
# Well, broadly. It definitely does have models, but what Django calls views are really controllers,
# and the view part is actually provided by the templates.

# Django’s main job is to decide what to do when a user asks for a particular URL on our site.
# Django’s workflow goes something like this:
#
# 1. An HTTP request comes in for a particular URL.
#
# 2. Django uses some rules to decide which view function should deal with the request
# (this is referred to as resolving the URL).
#
# 3. The view function processes the request and returns an HTTP response.



