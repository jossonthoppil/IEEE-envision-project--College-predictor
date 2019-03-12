from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.db.models.signals import post_save
from .all_choices import COLLEGE_CHOICES,COLLEGE_SELECTED
from multiselectfield import MultiSelectField


# Create your models here.
class FillProfile(models.Model):
	adv_air=models.IntegerField(default=0)
	mains_air=models.IntegerField(default=0)

#Assume you have an Author model that is a ForeignKey in a Book model. Now, if you delete an instance of the Author model, 
#Django would not know what to do with instances of the Book model that depend on that instance of Author model.
#The on_delete method tells Django what to do in that case. Setting on_delete=models.CASCADE will instruct Django 
#to cascade the deleting effect i.e. delete all the Book model instances that depend on the Author model instance you
#deleted.
	Logged_in_user=models.ForeignKey(User,on_delete=models.CASCADE,default=None)
	state_choices=(
				('select','Select your Home State'),
  				('andhra pradesh','Andhra Pradesh'),
                ('arrunachal pradesh','Arrunachal Pradesh'),
                ('assam','Assam'),
                ('bihar','Bihar'),
                ('chattisgarh','Chattisgarh'),
           		('goa','Goa'),
                ('gujrat','Gujrat'),
                ('haryana','Haryana'),
                ('himachal pradesh','Himachal Pradesh'),
                ('jammu & kashmir','Jammu & Kashmir'),
                ('jharkhand','Jharkhand'),
                ('karnataka','Karnataka'),
                ('kerala','Kerala'),
                ('madhya pradesh','Madhya Pradesh'),
                ('maharashtra','Maharashtra'),
                ('manipur','Manipur'),
                ('meghalaya','Meghalaya'),
                ('mizoram','Mizoram'),
                ('nagaland','Nagaland'),
                ('odisha','Odisha'),
                ('rajasthan','Rajasthan'),
                ('sikkim','Sikkim'),
                ('tamil nadu','Tamil Nadu'),
                ('telangana','Telangana'),
                ('tripura','Tripura'),
                ('uttarakhand','Uttharakhand'),
                ('uttar pradesh','Uttar Pradesh'),
                ('west bengal','West Bengal'),

				)
	state=models.CharField(max_length=100,choices=state_choices,default='select')
	category_choices=(
					('select category','Select your Category'),
					('general','General'),
					('general-pwd','General-PwD'),
					('obc-ncl','OBC-NCL'),
					('obc-ncl-pwd','OBC-NCL-PWD'),
					('sc','SC'),
					('st','ST'),

					)
	category=models.CharField(max_length=100,choices=category_choices,default='select category')
	
	Gender_choices=(
					(True,'Male'),
					(False,'Female'),
					)
	gender=models.BooleanField(choices=Gender_choices,default=True)
	


class FillPrefer(models.Model):
    college_choices=MultiSelectField(choices=COLLEGE_CHOICES,default='c1')
    college_selected=MultiSelectField(choices=COLLEGE_SELECTED,default='c6')
    Logged_in_user=models.ForeignKey(User,on_delete=models.CASCADE,default=None)

		