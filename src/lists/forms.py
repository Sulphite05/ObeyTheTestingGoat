from django import forms
from lists.models import Item

EMPTY_ITEM_ERROR = "You can't have an empty list item"
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




