"""URLS for user app"""
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import SignUpView, CustomerList, CustomerListRest, CustomerDetailRest, RegisterApi#, CustomerCreate, CustomerDelete, CustomerUpdate, CustomerDetail 

urlpatterns = [
    #with templates
    path("signup/", SignUpView.as_view(), name="signup"),
    path("customer/", CustomerList.as_view(), name="customerlist"),
    # path("customer/create/", CustomerCreate.as_view(), name="customercreate"),
    # path("customer/detail/<int:pk>", CustomerDetail.as_view(), name="customerdetail"),
    # path("customer/update/<int:pk>", CustomerUpdate.as_view(), name="customerupdate"),
    # path("customer/delete/<int:pk>", CustomerDelete.as_view(), name="customerdelete"),
    #url rest
    path("signuprest", RegisterApi.as_view()),
    path("customerrest/", CustomerListRest.as_view()),
    path("customerrest/<int:pk>/", CustomerDetailRest.as_view()),
]