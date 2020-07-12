from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('test', views.test, name='test'),
    path('test4', views.test4, name='test4'),
    path('test5', views.test5, name='test5'),
    path('test6', views.test6, name='test6'),
    path('test7', views.test7, name='test7'),
    path('login', views.handleLogin, name='handleLogin'),
    path('logout', views.handleLogout, name='handleLogout'),
    path('signup', views.handleSignup, name='handleSignup'),
    path('image_metadata', views.image_metadata, name='image_metadata'),
    path('handle_annotation', views.handle_annotation, name='handle_annotation'),

    ]
