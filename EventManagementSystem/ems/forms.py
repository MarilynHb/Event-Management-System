from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.forms.widgets import PasswordInput, TextInput
from .models import UserProfile

class CreateUserForm(UserCreationForm):

    class Meta:
        model = UserProfile
        fields=['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

class ProfileCompletionForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['biography', 'phone', 'address', 'city', 'country']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(ProfileCompletionForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super(ProfileCompletionForm, self).save(commit=False)
        instance.username = self.user  # Change user to username
        if commit:
            instance.save()
        return instance

