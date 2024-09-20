from django.test import TestCase
from lists.models import Item, List
from django.core.exceptions import ValidationError # for django's validation error(saving empty list item)
from django.db.utils import IntegrityError # for databse's integrity error(saving None list item)


# Create your tests here.
class ListAndItemModelTest(TestCase):
    def test_saving_and_retrieving_items(self):
        my_list = List()
        my_list.save()

        first_item = Item()
        first_item.text = "The first (ever) list item"
        first_item.list = my_list
        first_item.save()

        second_item = Item()
        second_item.text = "Item the second"
        second_item.list = my_list
        second_item.save()

        saved_list = List.objects.get()
        self.assertEqual(saved_list, my_list)

        saved_items = Item.objects.all()    # returns QuerySet which is a list-like object
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]

        self.assertEqual(first_saved_item.text, "The first (ever) list item")
        self.assertEqual(first_saved_item.list, my_list)
        self.assertEqual(second_saved_item.text, "Item the second")
        self.assertEqual(second_saved_item.list, my_list)

    def test_cannot_ave_null_list_items(self):
        my_list = List.objects.create()
        item = Item(list=my_list, text=None)
        with self.assertRaises(IntegrityError):
            item.save()
        # try:
        #     item.save()
        #     self.fail('The save should have raised an exception')
        # except IntegrityError:
        #     pass

    def test_cannot_save_empty_list_items(self):
        my_list = List.objects.create()
        item = Item(list=my_list, text="")
        with self.assertRaises(ValidationError):
            item.full_clean()   # applies all validation tests(empty=False)

    def test_get_absolute_url(self):
        mylist = List.objects.create()
        self.assertEqual(mylist.get_absolute_url(), f"/lists/{mylist.id}/")

