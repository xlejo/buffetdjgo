from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model

)

User = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('El usuario no existe')
            if not user.is_active:
                raise forms.ValidationError('El usuario no está activo')
        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField(label='E-mail')
    email2 = forms.EmailField(label='Confirmar e-mail')
    password = forms.CharField(widget=forms.PasswordInput, label='Contraseña')

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'email2',
            'password'
        ]

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        if email != email2:
            raise forms.ValidationError("Los e-mail deben ser iguales")
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError(
                "El e-mail ya está registrado")
        return super(UserRegisterForm, self).clean(*args, **kwargs)