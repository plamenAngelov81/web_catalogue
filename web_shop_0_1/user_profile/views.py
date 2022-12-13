from django.contrib.auth import get_user_model, login
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from web_shop_0_1.user_profile.forms import CreateProfileForm

UserModel = get_user_model()


def index(request):
    return render(request, 'user_profile/index.html')


class AccountLogin(LoginView):
    template_name = 'user_profile/account_login.html'


class AccountRegisterView(generic.CreateView):
    template_name = 'user_profile/account_create.html'
    form_class = CreateProfileForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


class AccountLogOut(LogoutView):
    next_page = reverse_lazy('index')


class AccountDetailsView(generic.DetailView):
    template_name = 'user_profile/account_details.html'
    model = UserModel


class AccountEditView(generic.UpdateView):
    model = UserModel
    template_name = 'user_profile/account_edit.html'
    fields = ['username',
              'first_name',
              'last_name',
              'age',
              'image_url',
              'phone_number',
              'user_address',
              ]

    def get_success_url(self):
        return reverse_lazy('account details', kwargs={'pk': self.request.user.pk})


class AccountDeleteView(generic.DeleteView):
    template_name = 'user_profile/account_delete.html'
    model = UserModel
    success_url = reverse_lazy('index')
