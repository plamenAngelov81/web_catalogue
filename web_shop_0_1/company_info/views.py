from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render

from web_shop_0_1.company_info.forms import MessagesCreateForm
from web_shop_0_1.company_info.models import CompanyInfo


def show_company_info(request):
    work_time = CompanyInfo.objects.filter(work_time_name='Summer').get()
    context = {
        'work_time': work_time
    }
    return render(request, 'company_info/contact.html', context)


class MessagesCreateView(generic.CreateView):
    template_name = 'company_info/messages.html'
    form_class = MessagesCreateForm
    success_url = reverse_lazy('index')
