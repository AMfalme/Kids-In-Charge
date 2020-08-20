from django import forms

from contact.models import ContactPageMessage


class FlavourSuggestionForm(forms.ModelForm):
    """
    A form for sending the message. Here we're using a Django ModelForm, but this could
    be as simple or as complex as you like -
    see https://docs.djangoproject.com/en/1.9/topics/forms/
    """
    class Meta:
        model = ContactPageMessage
        fields = ['name', 'email', 'phone', 'message']
