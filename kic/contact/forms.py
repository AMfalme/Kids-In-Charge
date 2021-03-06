from django import forms

from contact.models import ContactPageMessage


class ContactMessageForm(forms.ModelForm):
    """
    A form for sending the message. Here we're using a Django ModelForm, but this could
    be as simple or as complex as you like -
    see https://docs.djangoproject.com/en/3.1/topics/forms/modelforms/#modelform
    """
    class Meta:
        model = ContactPageMessage
        fields = ['name', 'email', 'phone', 'message']
