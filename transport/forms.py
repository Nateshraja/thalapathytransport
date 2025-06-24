from django import forms
from .models import Trip

class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={
                'type': 'date',  # 📅 this makes it a calendar picker
                'class': 'form-control'
            }),
            # Add other fields as needed
        }
