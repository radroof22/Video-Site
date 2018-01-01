from django.contrib.auth.models import User
from django import forms
from . models import Video,Article

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ["username","email","password"]

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["video","context"]

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ["date","title","description","video","creator"]
