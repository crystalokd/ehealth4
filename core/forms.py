from django import forms
from django.forms import ModelForm
from .models import Profile, User





class ProfileForm(ModelForm):
	class Meta:
		model = Profile
		fields = (
			'first_name',
			'Stomach_ach',
			'Diarrheal',
			'Injuries',
			'Head_ache',
			'Cough',
		)

		