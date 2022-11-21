from django import forms
from .models import Customer, Librarian


class SignUpForm(forms.ModelForm):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password1 = forms.CharField(max_length=10)
    password2 = forms.CharField(max_length=10)
    class Meta:
        model = Customer
        fields = ('username','email','phone_number', 'national_code', 'password1', 'password2')
    def clean(self):
        cleaned_data = super(SignUpForm, self).clean()
        password = cleaned_data.get("password1")
        confirm_password = cleaned_data.get("password2")
        phone_number = cleaned_data.get("phone_number")
        national_code = cleaned_data.get("national_code")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )
        if not phone_number.isnumeric() or len(phone_number)!=11:
            raise forms.ValidationError(
                "phone number is not valid"
            )
        if not national_code.isnumeric():
            raise forms.ValidationError(
                "national code is not valid"
            )


class SignInForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)


class LibrarianForm(forms.ModelForm):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password1 = forms.CharField(max_length=10)
    password2 = forms.CharField(max_length=10)
    class Meta:
        model = Librarian
        fields = ('username','email','phone_number', 'national_code', 'password1', 'password2')

    def clean(self):
        cleaned_data = super(LibrarianForm, self).clean()
        password = cleaned_data.get("password1")
        confirm_password = cleaned_data.get("password2")
        phone_number = cleaned_data.get("phone_number")
        national_code = cleaned_data.get("national_code")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )
        if not phone_number.isnumeric() or len(phone_number)!=11:
            raise forms.ValidationError(
                "phone number is not valid"
            )
        if not national_code.isnumeric():
            raise forms.ValidationError(
                "national code is not valid"
            )