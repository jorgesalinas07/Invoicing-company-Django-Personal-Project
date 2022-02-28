#Django
from django.contrib.auth import authenticate, login
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views.generic import FormView, UpdateView, DetailView, DeleteView
from django.urls.base import reverse_lazy
from django.contrib.auth.decorators import login_required


#Local
from .models import Client
from users.forms import SignupForm


def login_view(request):
    """ Login view """

    if request.method == "POST":

        email = request.POST["email"]
        password = request.POST['password']
        client = authenticate(request, email=email, password=password)
        if client:

            login(request,client)
            pk = Client.objects.get(email = email).id
            #import ipdb;ipdb.set_trace()
            #return redirect('invoicing:ListBillView', client_id=pk)
            return redirect('users:menu', client_id=pk)
        else: 

            return render(request, 'users/login.html', {
                'error': 'Invalid username and password'
            })
    return render(request, 'users/login.html')


class LogoutView(LoginRequiredMixin,auth_views.LogoutView):
    """ Logout view """

    template_name = 'users/logged_out.html'


class SignupView(FormView):
    """ Signup view """

    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        """ Save form data """

        form.save()
        return super().form_valid(form)

    def get_initial(self):
        """ Set initial data in fields """

        initial_data = super(SignupView, self).get_initial()
        initial_data['email'] = 'example@example.com'
        return initial_data


class UpdateProfileView(LoginRequiredMixin,UpdateView):
    """ Update view """

    template_name = 'users/update_client.html'
    model = Client
    fields = ['first_name', 'last_name', 'email', 'document']
    success_url = reverse_lazy('users:login')


class ClientDetailView(LoginRequiredMixin, DetailView):
    """ Detail of the client """

    model = Client
    context_object_name='client'
    queryset = Client.objects.all()
    template_name = 'users/detail.html'


    def get_context_data(self, **kwargs):
        """ Add client's bills to context"""

        context = super().get_context_data(**kwargs)
        client_id = self.get_object().id
        context['bill_quantity'] = len(Client.objects.get(pk=client_id).bill_set.all())
        context['client_id'] = client_id
        return context


class DeleteClientView(LoginRequiredMixin, DeleteView):
    """ Delete client """

    model = Client
    success_url = reverse_lazy('users:login')


@login_required
def menu(request, client_id):
    """ Main menu with all options for client """

    return render(request, 'menu.html', {'client_id':client_id})