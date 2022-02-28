#Django
from django import views
from django.urls import path

#Local
from . import views

app_name = 'invoicing'

urlpatterns = [
        path(
        route = '<int:client_id>/create',
        view = views.createbillview,
        name='create',
        ),

        path(
                route='list/<int:client_id>',
                view = views.list_bill_view,
                name='ListBillView',
        ),
        
        path(
                route='<int:invoice_id>/<int:client_id>/<int:invoice_index>/detail/',
                view = views.billDetailView,
                name = 'detail',
        ),
        path(
                route = '<int:invoice_id>/<int:client_id>/update',
                view  = views.updatebillView,
                name = 'update',
        ),
        path(
                route = 'delete/<int:pk>',
                view  = views.DeleteInvoice.as_view(),
                name = 'delete',
        ),
]