from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from common.models import Info

class UserForm(UserCreationForm):
    email = forms.EmailField(label='이메일')

    class Meta:
        model = User
        fields =("username","password1","password2","email")

class UserInfoForm(forms.ModelForm):

    class Meta:
        model = Info
        fields = ['name','phoneNumber','address']

        labels={
            'name':'이름',
            'phoneNumber':'휴대폰 번호',
            'address':'주소',
        }