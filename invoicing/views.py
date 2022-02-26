#Django
from django.http import HttpResponse
from django.shortcuts import render, redirect

#Locales
from .forms import BillForm
from .models import Bill, Product
from users.models import Client

def createbillview(request, pk):

    if request.method=='POST':
        form = BillForm(request.POST)
        if form.is_valid():
            client = Client.objects.get(pk=pk)
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
            #import ipdb;ipdb.set_trace()
            for name, description in form_products.items():
                added = False
                for registred_product in registred_products:
                    if registred_product.name == name:
                        new_bill.product.add(Product.objects.get(name = registred_product.name))
                        added=True
                if added==False:
                    Product.objects.create(name = name, description = description)
                    new_bill.product.add(Product.objects.get(name = name))
            
            return redirect('invoicing:ListBillView', pk=pk)
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

def list_bill_view(request,pk):
    return HttpResponse({'hello':'world'})