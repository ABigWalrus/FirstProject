from django.shortcuts import render, get_object_or_404, redirect


from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import CreateUserForm


def home_view(request):
	if request.user.is_authenticated:
		user_obj = request.user.username
		auth = 1
	else:
		user_obj = 0
		auth = 0
	context = {
		"user_obj": user_obj,
		"auth":auth
	}

	return render(request, "main.html", context)


def user_registration_view(request):
	form = CreateUserForm()
	error=""
	if request.method == 'POST':
		form = CreateUserForm(request.POST)	
		if User.objects.filter(username = request.POST.get('username')).exists():
			error = "username"
		elif User.objects.filter(email = request.POST.get('email')).exists():
			error = "email"
		elif request.POST.get('password1') != request.POST.get('password2'):
				error = "password1"
		else:
			
			if form.is_valid():#form.is_valid()
				form.save()
				return redirect('success')
			
			else:
				error = "password2"


	context = {
		'form': form,
		'error': error,
	}
	return render(request, "registration_page.html", context)

def registration_success_view(request):
	if request.user.is_authenticated:
		auth = 1
	else:
		auth = 0
	context = {
		'auth': auth,
	}
	return render(request, "registration_success_page.html", context)

def user_logout_view(request):
	logout(request)
	return redirect('login')

def user_login_view(request):
	error = 0;
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user_log = authenticate(request, username = username, password = password)

		if user_log is not None: 
			login(request, user_log)
			return redirect('home')
		else:
			error = 1;
	context = {
		'error': error,
	}
	return render(request, "login_page.html", context)


def user_view(request, my_id):
	if request.user.is_authenticated:
		auth = 1
	else:
		auth = 0
	user_object = get_object_or_404(User, id = my_id)
	context = {
		"user_object": user_object,
		"auth":auth,
	}
	return render(request, "user.html", context)


def user_delete_view(request, my_id):
	if request.user.is_authenticated:
		auth = 1
	else:
		auth = 0
	user_object = get_object_or_404(User, id = my_id)
	if request.method == "POST":
		user_object.delete()
		return redirect('../../')
	context = {
		"user_object": user_object,
		"auth": auth,
	}
	return render(request, "user_delete_page.html", context)


def users_view(request): 
	if request.user.is_authenticated:
		auth = 1
	else:
		auth = 0
	users_query = User.objects.filter(is_superuser = False)
	context = {
		"users_query": users_query,
		"auth": auth,
	}
	return render(request, "users_query_page.html", context)