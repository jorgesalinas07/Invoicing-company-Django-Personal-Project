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
            client.bill_set_create(
                                company_name = request.POST['company_name'], 
                                nit = request.POST['nit'],
                                code = request.POST['code'],
                                )
            products= Product.objects.all()
            for product in products:
                if product.name == request.POST['name_product1']:
                    pass
            return redirect('invoicing:ListBillView', pk=pk)
    else:
        form = BillForm()
        return render(request, 'invoicing/new.html', {
            'form': form,
        })

def list_bill_view(request,pk):
    return HttpResponse({'hello':'world'})