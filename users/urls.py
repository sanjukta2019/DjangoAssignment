# -*- coding: utf-8 -*-

from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.UserListView.as_view()),
    path('change-password', views.ChangePasswordView.as_view(), name='change-password'),
]