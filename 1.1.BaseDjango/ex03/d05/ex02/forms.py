from django import forms


class MessageForm(forms.Form):
    message = forms.CharField(label="Message", max_length=4000, required=True)
