from django import forms
from .models import Wish

class WishForm(forms.ModelForm):
    class Meta:
        model = Wish
        fields = ['wishtitle', 'mywish', 'deadline']
        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'date'})
        }
