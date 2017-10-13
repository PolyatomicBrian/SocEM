from django.forms import ModelForm
from django.forms import PasswordInput
from django.forms import EmailInput
from django.forms import TextInput
from django.forms import Textarea

from models import Identity
from models import Email

# Form class for Identity
class IdentityForm(ModelForm):
    class Meta:
        model = Identity
        fields = ['email', 'password']
        widgets = {
            'email'    : EmailInput(attrs={'placeholder' : 'Email'}),
            'password' : PasswordInput(attrs={'placeholder' : 'Password'}),
        }


# Form class for emails
class EmailForm(ModelForm):
    class Meta:
        model = Email
        fields = ['subject', 'header', 'content', 'signature']
        widgets = {
            'subject'   : TextInput(attrs={'placeholder' : 'Subject'}),
            'header'    : TextInput(attrs={'placeholder' : 'Header'}),
            'content'   : Textarea(attrs={'placeholder' : 'Content'}),
            'signature' : TextInput(attrs={'placeholder' : 'Signature'}),
        }
