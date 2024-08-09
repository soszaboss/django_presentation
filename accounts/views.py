from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import LoginForm, RegistrationForm
from .models import Account
from django.shortcuts import redirect


# la logique d'authetification peut-etre gere par des class predefinis qui gere ça pour vous


class Login(LoginView):
    form_class = LoginForm
    template_name = 'auth/login.html'
    next_page = reverse_lazy('books')
    redirect_authenticated_user = reverse_lazy('books')


class RegisterView(CreateView):
    form_class = RegistrationForm
    template_name = 'auth/register.html'
    success_url = reverse_lazy('login')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        print(form)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = Account.objects.create_user(email=email, password=password, username=username)
            user.save()
            return redirect(self.success_url)
        print(form.errors)
        return super().post(request, *args, **kwargs)


class Logout(LogoutView):
    next_page = reverse_lazy('login')

