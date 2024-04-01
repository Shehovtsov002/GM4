from django.contrib.auth.forms import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView
from . import models, forms


class RegisterView(CreateView):
    # form_class = UserCreationForm
    form_class = forms.CustomUserCreationForm
    template_name = 'registration/register.html'

    def get_success_url(self):
        return reverse('person:login')


class AuthorizationView(LoginView):
    form_class = AuthenticationForm
    template_name = 'registration/login.html'

    def get_success_url(self):
        return reverse('person:person_list')


class AuthLogoutView(LogoutView):
    next_page = reverse_lazy('person:login')


class PersonListView(ListView):
    template_name = 'registration/person_list.html'
    context_object_name = 'person'
    # model = User
    model = models.CustomUser

    def get_queryset(self):
        return self.model.objects.all()
