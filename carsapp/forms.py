from django import forms
from carsapp import models

class CarModelForm(forms.ModelForm):
    class Meta:
        model = models.Car
        fields = ['title', 'link', 'company', 'year', 'engine_type']