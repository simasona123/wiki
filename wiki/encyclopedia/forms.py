from django import forms


class Search(forms.Form):
    title = forms.CharField(max_length=30, widget=forms.TextInput(
        attrs={
            'class': 'search',
            'placeholder': 'SEARCH'
        }))


class New_Page(forms.Form):
    title = forms.CharField(label='Input Title: ', max_length=30, required=True, widget=forms.TextInput(
        attrs={
            'class': 'input',
            'placeholder': 'Input Title',
        }))
    text = forms.CharField(label='Input Text: ', widget=forms.Textarea(
        attrs={
            'placeholder': 'Markdown Language'
        }))


class Edit (forms.Form):
    text = forms.CharField(label='Input Text: ', widget=forms.Textarea(
        attrs={
            'placeholder': 'Markdown Language'
        }))
