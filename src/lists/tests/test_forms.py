from django.test import TestCase
from lists.forms import ItemForm

class Item_Form_Test(TestCase):
    def test_form_renders_item_text_input(self):
        form = ItemForm()
        self.assertIn('placeholder="Enter a to-do list item"', form.as_p())  # form.as_p() renders the form as html
        self.assertIn('class="form-control form-control-lg"', form.as_p())

    def test_form_validation_for_blank_items(self):
        form = ItemForm(data={"text":""})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["text"], ["You can't have an empty list item"])
        # form.save()
