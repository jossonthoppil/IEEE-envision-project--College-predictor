from django.shortcuts import render,redirect
from . import forms
from . models import FillProfile
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='ACCOUNTS:login')
def profile_views(request):
	if request.method=='POST':
		form=forms.FillProfileForm(request.POST)
		if form.is_valid():
			instance=form.save(commit=False)
			instance.Logged_in_user=request.user
			instance.save()
			return redirect('USER_DETAILS:userpreferences')
	else:
		form=forms.FillProfileForm()
	return render(request,'user_details/Fillprofile.html',{'ProfileForm':form})


@login_required(login_url='ACCOUNTS:login')
def preferences_views(request):
	if request.method=='POST':
		form=forms.FillPreferForm(request.POST)
		if form.is_valid():
			instance=form.save(commit=False)
			instance.Logged_in_user=request.user
			instance.save()
			return redirect('HOME:homepage')
	else:
		form=forms.FillPreferForm()
	return render(request,'user_details/Fillpreferences.html',{'PreferForm':form})