from django import forms


class CouponApplyForms(forms.Form):
    code = forms.CharField(label='Промокод')
