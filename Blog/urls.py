from django.contrib import admin
from django.urls import path

from .views import (
		user_view,
		users_view,
		user_delete_view,
		user_login_view,
		user_logout_view,
		registration_success_view,
		chat_view,
		timer_view,
	)

urlpatterns = [
    	path('users/<int:my_id>/', user_view),
    	path('users/<int:my_id>/delete/', user_delete_view),
    	path('users/', users_view),
    	path('login/', user_login_view, name = "login"),
    	path('logout/', user_logout_view, name = "logout"),
    	path('chat/', timer_view, name = "chat"),
    ]