from django.forms import ModelForm
from django import forms
from main.models import CarItems

class CarItemsForm(ModelForm):
    class Meta:
        model = CarItems
        fields = ["name", "price", "description", "model_number", "user_reviews", "image_url"]
        widgets = {
            'image_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter Image URL'}),
        }