from django import forms
from django.contrib.auth import get_user_model

from users.models import User


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)

    def clean_username(self):
        user_model = get_user_model()
        try:
            user_model.objects.get(username__iexact=self.cleaned_data['username'])
        except user_model.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError("Этот пользователь уже существует.")

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Пароли не совпадают.")
        return cd['password2']
