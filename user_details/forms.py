from django import forms
from . import models
from .all_choices import COLLEGE_CHOICES,COLLEGE_SELECTED
from django.contrib.auth.models import User

class FillProfileForm(forms.ModelForm):
	class Meta:
		model=models.FillProfile
		widgets = {
            'gender': forms.RadioSelect
        }
		fields=['adv_air','mains_air','state','category','gender']


class FillPreferForm(forms.ModelForm):
	class Meta:
		model=models.FillPrefer
		widgets={

	'college_choices': forms.SelectMultiple(attrs={'placeholder':'Fill your preferences','id':'lstbox1', 'class':'form-control' } ),
	'college_selected': forms.SelectMultiple(attrs={'placeholder':'Fill your preferences','id':'lstbox2', 'class':'form-control' } )
		}
		fields=['college_choices','college_selected']