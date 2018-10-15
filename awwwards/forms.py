from django import forms
from .models import *

class NewPostForm(forms.ModelForm):
    class Meta :
        model = Projects
        exclude = ['user', 'post_date','liker']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']