from django import forms

class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(
        label='Количество',
        widget=forms.NumberInput(attrs={'min': 1, 'max': 10000, 'type': 'number', 'value': 1}),
    )
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
