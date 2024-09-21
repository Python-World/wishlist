from django import forms
from .models import Wish

class WishForm(forms.ModelForm):
    class Meta:
        model = Wish
        fields = ["wishtitle", "mywish", "deadline"]  # Fields displayed in the form
        widgets = {"deadline": forms.DateInput(attrs={"type": "date"})}  # Custom date input widget
