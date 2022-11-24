from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        widget =forms.TextInput(
            attrs = {'placeholder': 'Ваше имя', 'class': 'form-control'}
        )
    )
    phone = forms.IntegerField(
        widget=forms.NumberInput(
        attrs={'placeholder': 'Номер Телефона', 'class': 'form-control', 'pattern':'\+?[0-9\s\-\(\)]+',}
    )
    )
    message = forms.CharField(
        max_length = 200,
        widget = forms.Textarea(attrs={'placeholder': 'Подробнее', 'class': 'form-control'}),
        required= False
    )