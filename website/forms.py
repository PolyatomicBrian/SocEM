from django.forms import ModelForm
from django.forms import PasswordInput
from django.forms import EmailInput

from models import Identity

# Form class for Identity
class IdentityForm(ModelForm):
    class Meta:
        model = Identity
        fields = ['email', 'password']
        widgets = {
            'email'    : EmailInput(attrs={'placeholder' : 'Email'}),
            'password' : PasswordInput(attrs={'placeholder' : 'Password'}),
        }
