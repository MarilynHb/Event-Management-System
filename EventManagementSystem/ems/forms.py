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
        if self.user:
            user_profile = self.user
            self.fields['biography'].initial = self.user.biography
            self.fields['phone'].initial = self.user.phone
            self.fields['address'].initial = self.user.address
            self.fields['city'].initial = self.user.city
            self.fields['country'].initial = self.user.country

    def save(self, commit=True):
        instance = super(ProfileCompletionForm, self).save(commit=False)
        if self.user:
            user_profile = UserProfile.objects.get(pk=self.user.pk)  # Retrieve the user's profile
            user_profile.biography = instance.biography
            user_profile.phone = instance.phone
            user_profile.address = instance.address
            user_profile.city = instance.city
            user_profile.country = instance.country
            if commit:
                user_profile.save()
        return instance

