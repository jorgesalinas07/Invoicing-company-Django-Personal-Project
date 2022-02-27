#Django
from django.contrib.auth import authenticate, login
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views.generic import FormView, UpdateView, DetailView
from django.urls.base import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.urls import reverse


#Local
from .models import Client

#Local
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
            return redirect('invoicing:ListBillView', client_id=pk)
        else: 
            return render(request, 'users/login.html', content_type={
                'error': 'Invalid username and password'
            })
    return render(request, 'users/login.html')


class LogoutView(LoginRequiredMixin,auth_views.LogoutView):
    template_name = 'users/logged_out.html'

class SignupView(FormView):
    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        """ Save form data """
        form.save()
        return super().form_valid(form)

    def get_initial(self):
        initial_data = super(SignupView, self).get_initial()
        initial_data['email'] = 'example@example.com'
        return initial_data


class UpdateProfileView(LoginRequiredMixin,UpdateView):
    pass

class UserDetailView(LoginRequiredMixin, DetailView):
    pass