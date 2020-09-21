from django.urls import path

from . import views

urlpatterns = [
    path("", views.input, name='main'),
    path("<str:short_url>", views.goto, name='redirect')
]
