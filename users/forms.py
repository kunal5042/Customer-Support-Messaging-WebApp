from django.forms import ModelForm
from django import forms
from users.models import UserQuery

CANNED_MESSAGES = [

]

class UserForm(ModelForm):
    class Meta:
        model = UserQuery
        fields = ['userID', 'messageBody']

class ResolveQuery(forms.Form):
    response = forms.CharField(required=True, widget=forms.Textarea)
