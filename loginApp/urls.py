from django.conf.urls import include,url
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^login$', views.loginFormView.as_view(),name='login_form'),
    url(r'^register$',views.registerFormView.as_view(),name='register_form'),
    url(r'^checkRegister',views.checkRegisterView),
    url(r'^checkLogin',views.checkLoginView),
    url(r'^space', views.spaceView),
        ]
