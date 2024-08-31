from django.test import TestCase
# from django.http import HttpRequest
# from lists.views import home_page
from lists.models import Item


# Create your tests here.
class HomePageTest(TestCase):
    def test_uses_home_template(self):
        # request = HttpRequest()
        # response = home_page(request)
        # html = response.content.decode("utf-8")
        # self.assertIn("<title>To-Do lists</title>", html)
        # self.assertTrue(html.startswith("<html>"))
        # self.assertTrue(html.endswith("</html>"))

        # response = self.client.get("/")
        # self.assertContains(response, "<title>To-Do lists</title>")
        # self.assertContains(response, "<html>")
        # self.assertContains(response, "</html>")
        # self.assertTemplateUsed(response, "home.html")
        response = self.client.get("/")
        self.assertTemplateUsed(response, "home.html")

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

    def test_displays_all_list_items(self):
        Item.objects.create(text="itemey 1")
        Item.objects.create(text="itemey 2")
        response = self.client.get("/")
        self.assertContains(response, "itemey 1")
        self.assertContains(response, "itemey 2")

    def test_can_save_post_request(self):
        self.client.post("/", data={"item_text": "A new list item"})

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, "A new list item")

    def test_redirects_after_POST(self):
        response = self.client.post("/", data={"item_text": "A new list item"})
        self.assertRedirects(response, "/")

    def test_only_saves_item_when_necessary(self):
        self.client.get("/")
        self.assertEqual(Item.objects.count(), 0)


class ItemModelTest(TestCase):
    def test_saving_and_retrieving_item(self):
        first_item = Item()
        first_item.text = "The first (ever) list item"
        first_item.save()

        second_item = Item()
        second_item.text = "Item the second"
        second_item.save()

        saved_items = Item.objects.all()    # returns QuerySet which is a list-like object
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]

        self.assertEqual(first_saved_item.text, "The first (ever) list item")
        self.assertEqual(second_saved_item.text, "Item the second")



