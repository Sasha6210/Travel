from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()

class ContactForm(forms.Form):
    name = forms.CharField(
        min_length = 2,
        widget = forms.TextInput(
            attrs = {
                "placeholder": "Your Name",
                "class": "form-input",
                "id": "contact-your-name-2",
                "data-constraints": "@Required"
            }
        )
    )
    email = forms.EmailField(
        widget = forms.EmailInput(
            attrs = {
                "placeholder": "Email",
                "class": "form-input",
                "id": "contact-email-2",
                "data-constraints": "@Email @Required"
            }
        )
    )
    phone = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                "placeholder": "Phone",
                "class": "form-input",
                "id": "contact-phone-2",
                "data-constraints": "@Numeric"
            }
        )
    )
    text = forms.CharField(
        widget = forms.Textarea(
            attrs = {
                "placeholder": "Message",
                "class": "form-input",
                "id": "contact-message-2",
                "data-constraints": "@Required"
            }
        )
    )
    

class UserRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model=User