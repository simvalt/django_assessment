from django.urls import path
from webApp.api.views import CustomersApiView, PaymentsCustomersApiView, CustomersDetailApiView, PaymentsCustomersDetailApiView

urlpatterns = [
    path('', CustomersApiView.as_view(), name='customers-list'),
    path('<int:pk>', CustomersDetailApiView.as_view(), name='customer-detail'),
    path('payments/', PaymentsCustomersApiView.as_view(), name='payments-list'),
    path('payments/<int:pk>', PaymentsCustomersDetailApiView.as_view(), name='payment-detail'),
]