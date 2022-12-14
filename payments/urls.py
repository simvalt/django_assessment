"""URLS for payments app"""
from django.urls import path

from .views import PaymentsCustomerListRest, PaymentsCustomerDetailRest

urlpatterns = [
    path("list/", PaymentsCustomerListRest.as_view()),
    path("detail/<int:pk>/", PaymentsCustomerDetailRest.as_view()),
]