from django.forms import ModelForm
from main.models import CarItems

class CarItemsForm(ModelForm):
    class Meta:
        model = CarItems
        fields = ["price", "description", "model_number", "user_reviews"]