#Django
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Bill
from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

#Locales
from .forms import BillForm
from .models import Bill, Product
from users.models import Client

def createbillview(request, client_id):

    if request.method=='POST':
        form = BillForm(request.POST)
        if form.is_valid():
            client = Client.objects.get(pk=client_id)
            client.bill_set.create(
                                company_name = request.POST['company_name'], 
                                nit = request.POST['nit'],
                                code = request.POST['code'],
                                )
            
            registred_products= Product.objects.all()
            
            new_bill = Bill.objects.get(nit=request.POST['nit'])
            form_products = {request.POST['name_product1']:request.POST['description_product1'],
                             request.POST['name_product2']:request.POST['description_product2'],
                             request.POST['name_product3']:request.POST['description_product3']}
            for name, description in form_products.items():
                added = False
                for registred_product in registred_products:
                    if registred_product.name == name:
                        new_bill.product.add(Product.objects.get(name = registred_product.name))
                        added=True
                if added==False:
                    Product.objects.create(name = name, description = description)
                    new_bill.product.add(Product.objects.get(name = name))
            
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
    form = BillForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        data = form.cleaned_data
        client = Client.objects.get(pk=client_id)
        bill = client.bill_set.all().get(pk=invoice_id)
        bill.company_name = data['company_name']
        bill.nit = data['nit']
        bill.code = data['code']
        #product_exitance(data['name_product1'])
        return render(request, 'invoicing/update.html',{'form':form})
    else:
        return render(request, 'invoicing/update.html',{'form':form})
        
        

@login_required
def list_bill_view(request,client_id):
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

class DeleteBillView(LoginRequiredMixin, DeleteView):
    pass


def product_exitance(product_name):
    """ """
    existance = False

    for bill in Bill.objects.all():

        for product in bill.product.all():

            if product.name == product_name:
                existance = True
                break
    
    return existance