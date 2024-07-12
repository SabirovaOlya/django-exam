from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, View, CreateView
from .models import User, Product
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import UserRegisterModelForm
from .tasks import send_notification_mail


class ProductListView2(ListView):
    queryset = Product.objects.all()
    template_name = 'index.html'
    model = Product
    context_object_name = 'products'


class ProductListView(LoginRequiredMixin, DetailView):
    queryset = User.objects.all()
    template_name = 'index.html'
    success_url = reverse_lazy('settings_page')

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['products'] = Product.objects.all()
        return context


class RegisterCreateView(CreateView):
    template_name = 'auth/register.html'
    form_class = UserRegisterModelForm
    success_url = reverse_lazy('product_list_page')
    redirect_authenticated_user = True,
    next_page = 'product_list_page'

    def form_valid(self, form):
        form.save()
        send_notification_mail.delay(
            target_mail=form.data['email'],
            message='Successfully registered'
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('product_list_page')
