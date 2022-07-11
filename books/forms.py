from django import forms


class ReviewForm(forms.Form):
    text = forms.CharField(label='Text')
    rating = forms.IntegerField(label='Rating', max_value=5, min_value=1)