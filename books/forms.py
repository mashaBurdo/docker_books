from django import forms
from django.utils.translation import gettext as _


class ReviewForm(forms.Form):
    text = forms.CharField(label=_("Text"))
    rating = forms.IntegerField(label=_("Rating"), max_value=5, min_value=1)


class BookForm(forms.Form):
    name = forms.CharField(label=_("Name"))
    author = forms.CharField(label=_("Author"), required=False)
    price = forms.IntegerField(label=_("Price"))
    pages = forms.IntegerField(label=_("Pages"), required=False)


class LoginForm(forms.Form):
    username = forms.CharField(label=_("Username"))
    password = forms.CharField(label=_("Password"), widget=forms.PasswordInput)


class RegistrationForm(LoginForm):
    email = forms.EmailField(label=_("Email"))