from django import forms
#from django.contrib.auth.models import User
from .models import UserProfileInfo

class modform(forms.ModelForm):
    #password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = "__all__"

'''class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic
'''
