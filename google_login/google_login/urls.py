from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from g_login.views import index, login

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login", login),
    path("home_page", index),
    path(r"^auth/", include("social_django.urls", namespace="social")),
]
