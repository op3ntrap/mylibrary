from django.forms import ModelForm, forms
from .models import *
# from captcha.fields import CaptchaField
from django.contrib.auth.models import User
# import string
import re


class profile_form(ModelForm):
	class Meta:
		model = Member
		exclude = ['user', 'membership', 'membership_type', 'profile_pic']


class librarian_form(ModelForm):
	class Meta:
		model = Librarian
		exclude = ['profile_pic', 'book_recommendations', 'role', 'user']


def username_check(param):
	queryset = User.objects.filter(username=param)
	if len(queryset) == 0:
		return True
	else:
		return False


def password_check(param):
	# parts = [string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation]
	import re
	password = param
	p = re.compile('^(?=.*[!$?])(?=.*[a-z])(?=.*[A-Z]).{8}$')
	if re.search(p, param):
		return True
	else:
		return False


class member_sign_up_form(profile_form):
	from django import forms

	username = forms.CharField(max_length=255)
	user_password = forms.CharField(widget=forms.PasswordInput())

	def clean_username(self):
		data = self.cleaned_data['username']
		if not username_check(data):
			raise forms.ValidationError('Sorry this Username is already taken')
		return data

	def clean_user_password(self):
		data = self.cleaned_data['user_password']
		if not password_check(data):
			raise forms.ValidationError(
					'Sorry this Password is not strong enough.Please include lowercase, Uppercase, number and a special character')
		return data
