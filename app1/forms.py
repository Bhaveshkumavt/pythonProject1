from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
# from ecompages.models import User, Profile
from django.contrib.auth.forms import UserCreationForm
from allauth.account.forms import SignupForm
from app1.models import Profile, Notice
# from django.contrib.auth.forms import AuthenticationForm
# from django.utils.translation import ugettext_lazy as _

# class AuthenticationRememberMeForm(AuthenticationForm):
#     remember_me = forms.BooleanField(label=_('Remember Me'), initial=False,
#                                      required=False)

class RegistrationForm(SignupForm):
    class Meta():
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['username'].label = 'Display Name'
            self.fields['Email'].label = "Email Address"


# class ProfileForm(forms.ModelForm):
#     class Meta():
#         model = Profile
#         fields = ['name','gender','address']
#
#
#
