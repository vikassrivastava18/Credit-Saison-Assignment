from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("api_1/<str:card_num>", views.Searched, name='searched')
]
