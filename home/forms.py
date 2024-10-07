from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order  # Link the form to the Order model
        fields = ['name', 'village', 'age']  # Include fields from the Order model
        labels = {
            'name': 'Your Name',
            'village': 'Your Village',
            'age': 'Your Age'
        }
