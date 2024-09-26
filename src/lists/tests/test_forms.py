from django.test import TestCase
from lists.forms import ItemForm
from lists.models import Item, List


class Item_Form_Test(TestCase):
    def test_form_renders_item_text_input(self):
        form = ItemForm()
        self.assertIn('placeholder="Enter a to-do list item"', form.as_p())  # form.as_p() renders the form as html
        self.assertIn('class="form-control form-control-lg"', form.as_p())

    def test_form_validation_for_blank_items(self):
        form = ItemForm(data={"text":""})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["text"], ["You can't have an empty list item"])

    def test_form_save_handles_saving_to_a_list(self):
        my_list = List.objects.create()
        form = ItemForm(data={"text": "do me"})
        new_item = form.save(for_list=my_list)
        self.assertEqual(new_item, Item.objects.get())
        self.assertEqual(new_item.text, "do me")
        self.assertEqual(new_item.list, my_list)

