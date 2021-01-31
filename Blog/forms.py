from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Message

class CreateUserForm(UserCreationForm):
	username = forms.CharField(	widget = forms.TextInput(attrs = {"placeholder":"Имя Пользователя","class":"field"}))
	email = forms.EmailField(widget = forms.EmailInput(attrs = {"placeholder":"Почта","class":"field"}))
	first_name = forms.CharField(widget = forms.TextInput(attrs = {"placeholder":"Имя","class":"field"}))
	last_name = forms.CharField(widget = forms.TextInput(attrs = {"placeholder":"Фамилия","class":"field"}))
	password1 = forms.CharField(widget = forms.PasswordInput(attrs = {"placeholder":"Пароль","class":"field"}))
	password2 = forms.CharField(widget = forms.PasswordInput(attrs = {"placeholder":"Повторите пароль","class":"field"}))
	class Meta:
		model = User
		fields = [
			'username', 
			'email',
			'first_name',
			'last_name',
			'password1',
			'password2',
		]

class MessageForm(forms.ModelForm):
	content = forms.CharField(widget = forms.TextInput())
	class Meta:
		model = Message
		fields = [
			'content',
		]

	# def clean(self):
 #       email = self.cleaned_data.get('email')
 #       if User.objects.filter(email=email).exists():
 #            raise ValidationError("Email exists")
 #       return self.cleaned_data