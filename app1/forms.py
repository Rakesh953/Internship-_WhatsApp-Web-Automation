from django import forms
from app1.models import *

class registerform(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','password']
        widgets={'password':forms.PasswordInput()}

class profileform(forms.ModelForm):
    class Meta:
        model=profile
        fields=['profile_pic','about']
        
