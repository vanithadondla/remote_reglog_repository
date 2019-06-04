from django import forms
class RegistrationForm(forms.Form):
    first_name=forms.CharField(
        label="enter your firstname",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'your firstname'
            }
        )
    )
    last_name = forms.CharField(
        label="enter your lastname",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your lastname'
            }
        )
    )
    mobile = forms.IntegerField(
        label="enter your mobile number",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your mobile number'
            }
        )
    )
    email = forms.EmailField(
        label="enter your email id",
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your email id'
            }
        )
    )
    username = forms.CharField(
        label="enter your username",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your username'
            }
        )
    )
    password1 = forms.CharField(
        label="enter your password",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your password '
            }
        )
    )
    password2 = forms.CharField(
        label="enter Confirmation Password",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Confirmation Password'
            }
        )
    )
class LoginForm(forms.Form):
    username = forms.CharField(
        label="enter your username",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your username'
            }
        )
    )
    password1 = forms.CharField(
        label="enter your password",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your password'
            }
        )
    )