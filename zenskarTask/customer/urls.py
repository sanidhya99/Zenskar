from .views import *

from django.urls import path

urlpatterns=[
    path("customer/" ,CustomerCreateView.as_view(),name="CustomerCreation"),
    path("customer/delete/" ,CustomerEditView.as_view(),name="CustomerUpdate"),
            ]