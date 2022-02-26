from django import forms


class BillForm(forms.Form):

    company_name = forms.CharField(min_length=4, max_length=50)
    nit = forms.CharField(min_length=2, max_length=10)
    code = forms.IntegerField()
    name_product1 = forms.CharField(min_length=4, max_length=50)
    description_product1 = forms.CharField(min_length=4, max_length=50)
    name_product2 = forms.CharField(min_length=4, max_length=50)
    description_product2 = forms.CharField(min_length=4, max_length=50)
    name_product3 = forms.CharField(min_length=4, max_length=50)
    description_product3 = forms.CharField(min_length=4, max_length=50)