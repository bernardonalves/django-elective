from django.urls import path

from . import views


app_name = 'usersapp'

urlpatterns = [
    path('', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('signup', views.signup, name='signup'),
    path('password_reset', views.password_reset, name='password_reset'),
]