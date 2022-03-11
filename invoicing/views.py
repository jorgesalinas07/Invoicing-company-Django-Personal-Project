#Django
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .models import Bill
from django.views.generic import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

#Locales
from .forms import BillForm
from .models import Bill, Product
from users.models import Client


@login_required
def createbillview(request, client_id):
    """ Create a new bill """

    if request.method=='POST':
        form = BillForm(request.POST)
        if form.is_valid():
            client = Client.objects.get(pk=client_id)
            client.bill_set.create(
                                company_name = request.POST['company_name'], 
                                nit = request.POST['nit'],
                                code = request.POST['code'],
                                )
            product1 = Product.objects.create(name = request.POST['name_product1'], description = request.POST['description_product1'])
            product2 = Product.objects.create(name = request.POST['name_product2'], description = request.POST['description_product2'])
            product3 = Product.objects.create(name = request.POST['name_product3'], description = request.POST['description_product3'])
            new_bill = Bill.objects.get(nit=request.POST['nit'])
            new_bill.product.add(product1, product2, product3)
            
            return redirect('invoicing:ListBillView', client_id=client_id)
        else:
            form = BillForm()
            return render(request, 'invoicing/new.html', {
                'form': form,
                'error_mesage': 'Here goes the error mensage'
            })
    else:
        form = BillForm()
        return render(request, 'invoicing/new.html', {
            'form': form,
        })


@login_required
def updatebillView(request, invoice_id, client_id):
    """Update a bill"""

    form = BillForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            data = form.cleaned_data
            client = Client.objects.get(pk=client_id)
            bill = client.bill_set.all().get(pk=invoice_id)
            bill.company_name = data['company_name']
            bill.nit = data['nit']
            bill.code = data['code']
            for index, product in enumerate(bill.product.all(),1):
                if index == 1:
                    product1 = Product.objects.get(pk = product.id)
                    product1.name = data['name_product1']
                    product1.description = data['description_product1']
                if index == 2:
                    product2 = Product.objects.get(pk = product.id)
                    product2.name = data['name_product2']
                    product2.description = data['description_product2']
                if index == 3:
                    product3 = Product.objects.get(pk = product.id)
                    product3.name = data['name_product3']
                    product3.description = data['description_product3']
            bill.save()
            product1.save()
            product2.save()
            product3.save()
            return redirect('invoicing:ListBillView', client_id=client_id)
        else:
            return render(request, 'invoicing/update.html',{
                                                           'form':form,
                                                            'error_mensage': 'Here goes the error mesage'
                                                           })
    else:
        return render(request, 'invoicing/update.html',{'form':form})


class DeleteInvoice(DeleteView,LoginRequiredMixin):
    """ Delete a bill """

    model = Bill
    success_url = reverse_lazy('users:login')


@login_required
def list_bill_view(request,client_id):
    """ List all bills """

    query = Client.objects.get(pk=client_id)
    invoices_ids = []
    for id in query.bill_set.all():
        invoices_ids.append(id.pk)
    num_invoices = enumerate(invoices_ids,1)
    #num_invoices = range(1,len(query.bill_set.all()))
    #import ipdb;ipdb.set_trace()
    return render(request, 'invoicing/index.html', {
                'invoices': num_invoices,
                'first_name': query.first_name,
                'last_name': query.last_name,
                'document': query.document,
                'pk': query.pk,
                'client_id': client_id
                })


@login_required
def billDetailView(request, invoice_id, client_id, invoice_index):
    """ Detail of each bill """
    client = Client.objects.get(pk=client_id)
    bill = client.bill_set.all().get(pk=invoice_id)
    products = bill.product.all()
    return render(request, 'invoicing/detail.html',{
                                'invoice_id':invoice_id,
                                'products': products,
                                'nit':bill.nit,
                                'code':bill.code,
                                'company_name':bill.company_name,
                                'client_id':client_id,
                                'invoice_index': invoice_index
                                })


