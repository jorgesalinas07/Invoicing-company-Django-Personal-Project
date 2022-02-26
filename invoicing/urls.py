from django import views
from django.urls import path

from . import views

app_name = 'invoicing'

urlpatterns = [
        path(
        route = '<int:pk>/create',
        view = views.createbillview,
        name='create',),

        path(
        route='list/<int:pk>',
        view = views.list_bill_view,
        name='ListBillView',)
]