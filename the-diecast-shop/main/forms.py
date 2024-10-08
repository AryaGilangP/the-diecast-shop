from django.forms import ModelForm
from django import forms
from main.models import CarItems
from django.utils.html import strip_tags

class CarItemsForm(ModelForm):
    class Meta:
        model = CarItems
        fields = ["name", "price", "description", "model_number", "user_reviews", "image_url"]
        widgets = {
            'image_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter Image URL'}),
        }

    def clean_name(self):
        name = self.cleaned_data["name"]
        return strip_tags(name)

    def clean_description(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)