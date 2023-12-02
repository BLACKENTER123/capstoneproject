from django import forms
from .models import Bookings

class BookingForm(forms.ModelForm):
    """ form for bookings """
    class Meta:
        model = Bookings
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'please enter your name', 'class': 'form-control'}),
            'slots': forms.NumberInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control date'})
        }
        