from django import forms


class UserRegisterForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput, max_length=30, label='نام')
    last_name = forms.CharField(widget=forms.TextInput, max_length=50, label='نام خانوادگی')
    username = forms.CharField(widget=forms.TextInput, max_length=30, label='نام کاربری')
    email = forms.EmailField(widget=forms.EmailInput, max_length=50, label='ایمیل')
    password = forms.CharField(widget=forms.PasswordInput, max_length=50, label='رمز عبور')


class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput, max_length=30, label='نام کاربری')
    password = forms.CharField(widget=forms.PasswordInput, max_length=50, label='رمز عبور')
