# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render
from .forms import *
from django.contrib.auth.decorators import login_required
from .models import *
from django.apps import apps
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from silk.profiling.profiler import silk_profile


@silk_profile(name='View Base Template')
def view_base_template(request):
	return render(request, 'UserManager/base.html', context=None)


@silk_profile(name='sign up')
def sign_up(request):
	custom_form = member_sign_up_form
	if request.method == 'POST':
		custom_form = member_sign_up_form(request.POST)
		if custom_form.is_valid():
			new_user = User.objects.create(username=custom_form.cleaned_data.get('username'),
			                               password=custom_form.cleaned_data.get('user_password'))
			instance = custom_form.save(commit=False)
			instance.user = new_user
			instance.save()
			return redirect(to='/UserManager/login.html')
	return render(request, 'UserManager/sign_up.html', context={'form': custom_form})


@silk_profile(name='login')
@login_required(login_url='login')
def profile_view(request):
	if request.user.is_staff:
		form = librarian_form
	else:
		form = profile_form
	if request.method == 'POST':
		if request.user.is_staff:
			staff_user, created = Librarian.objects.get_or_create(user=request.user)
			form = librarian_form(request.POST, instance=staff_user)
			if form.is_valid():
				form.save()
				messages.success(request, 'Your Profile has been successfully modified')

		else:
			form = profile_form(request.POST)
			member_user, created = Member.objects.get_or_create(user=request.user)
			form = profile_form(request.POST, instance=member_user)
			if form.is_valid():
				form.save()
				messages.success(request, 'Your Profile has been successfully modified')
	return render(request, 'UserManager/profile.html', context={'form': form})


@silk_profile(name='Account Management View')
@login_required(login_url='login')
def account_management_view(request):
	returning_db = apps.get_model('TransactionManager', model_name='Returning')
	member = request.user.member
	user_lending_records = returning_db.objects.filter(client=member)
	user_lending_records_returned = user_lending_records.filter(returned=True)
	user_lending_records_not_returned = user_lending_records.filter(returned=False)
	context = {
		'lend'    : user_lending_records_not_returned,
		'returned': user_lending_records_returned
	}
	return render(request, 'UserManager/account_management.html', context=context)


"""
from datetime import datetime
from dateutil.relativedelta import relativedelta

date_after_month = datetime.today()+ relativedelta(months=1)
print 'Today: ',datetime.today().strftime('%d/%m/%Y')
print 'After Month:', date_after_month.strftime('%d/%m/%Y')
"""
