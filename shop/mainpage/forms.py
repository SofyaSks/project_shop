from django import forms
from django.contrib.auth.models import User

class UserLoginForm(forms.Form):
    username = forms.CharField(label='Имя пользователя')
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')

# как сказал чатГПТ лейблы работают только при наследовании от ModelForms
    # class Meta:
    #     labels = {
    #         'username': 'Имя пользователя',
    #         'password': 'Пароль'
    #     }

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(
        label='Пароль',
        widget= forms.PasswordInput
    )

    password2 = forms.CharField(
        label='Повтор пароля',
        widget= forms.PasswordInput
    )

    class Meta:
        model = User

        # почему не labels?
        fields = {
            'username': 'Логин',
            'first_name': 'Имя',
            'email': 'Электронная почта'
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords do not match')
        return cd['password2']