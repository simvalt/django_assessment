from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name="login"),
    path('dashboard/<int:id>/customers',views.customer_front, name="dashboard_customers"),
    path('dashboard/<int:id>/customers/<int:customer>/payments',views.payments_front, name="dashboard_payments"),
    path('customer/<int:id>/customers/create',views.customer_create,name="customer_create"),
    path('customer/<int:id>/customers/delete',views.customer_delete,name="customer_delete"),
    path('customer/<int:id>/customers/update',views.customer_update,name="customer_update"),
    path('customer/<int:id>/customers/<int:customer>/payments/create',views.payments_create,name="payments_create"),
    path('customer/<int:id>/customers/<int:customer>/payments/delete',views.payments_delete,name="payments_delete"),
    path('customer/<int:id>/customers/<int:customer>/payments/update',views.payments_update,name="payments_update"),
    path('api/login',views.api_login,name="api_login"),
    path('api/customers',views.api_customers,name="api_customers"),
    path('api/payments',views.api_payments,name="api_payments")
]