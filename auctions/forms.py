from django import forms
from django.forms import ModelForm
from django.forms.widgets import NumberInput
from .models import Auctions

class CreateForm(ModelForm):
    class Meta:
        model = Auctions
        fields = "__all__"
        widget = forms.DateTimeInput(attrs= {
        'input_type': 'text'
        })


    """
    CATEGORIES = (
    ('LAP', 'Laptop'),
    ('CTH', 'Clothing'),
    ('PRO', 'Properties'),
    ('Cat', 'No Category selected')
    )

    body = forms.CharField(widget=forms.Textarea({
        'name':'body',
        'id':'body'
        }))

    title = forms.CharField(max_length = 50,
         widget = forms.TextInput(attrs= {
        'name': 'title'
        }))
    price = forms.DecimalField(widget=forms.NumberInput(attrs={'name':'price'}))

    image = forms.ImageField(widget = forms.FileInput(attrs={'name': 'image'}))
    category = forms.ChoiceField(widget=forms.Select(), choices=CATEGORIES)
    """
"""
    user = forms.CharField(max_length=20,
         widget= forms.TextInput(attrs= {
        'name': 'username'}))

"""

"""
    class Meta:
        model = Topping
        fields = ('title', 'price')
        widgets = {
            'price': forms.NumberInput(attrs={'step': 0.25}),
        }
"""