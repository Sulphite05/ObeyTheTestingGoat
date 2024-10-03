from django import forms
from lists.models import Item
from django.core.exceptions import ValidationError

EMPTY_ITEM_ERROR = "You can't have an empty list item"
DUPLICATE_ITEM_ERROR = "You've already got this in your list"

class ItemForm(forms.models.ModelForm):
    class Meta:
        model = Item
        fields = ("text",)
        widgets = {
            "text": forms.widgets.TextInput(
                attrs={
                    "placeholder": "Enter a to-do list item",
                    "class": "form-control form-control-lg",
                }
            )
        }
        error_messages = {"text": {"required": EMPTY_ITEM_ERROR}}


    def save(self, for_list):
        self.instance.list = for_list # represents the database object that is being modified or created
        return super().save()

    # item_text = forms.CharField(
    #     widget=forms.widgets.TextInput(
    #         attrs={
    #             "placeholder": "Enter a to-do list item",
    #             "class": "form-control form-control-lg"
    #         }
    #     ),
    # )



class ExistingListItemForm(ItemForm):
    def __init__(self, for_list, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance.list = for_list

    def validate_unique(self):
        try:
            self.instance.validate_unique()
        except ValidationError as e:
            e.error_dict = {"text": [DUPLICATE_ITEM_ERROR]}
            self._update_errors(e)

    def save(self):
        return forms.models.ModelForm.save(self)




