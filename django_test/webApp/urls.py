from django.urls import path
from . import views
from webApp.views import home

urlpatterns = [
    path('', views.home),
    path('registrarCustomers/', views.registrarCustomers),
    path('editarCustomer/<id>', views.editarCustomer),
    path('editarCustomers/', views.editarCustomers),
    path('eliminarCustomer/<id>', views.eliminarCustomer),
]