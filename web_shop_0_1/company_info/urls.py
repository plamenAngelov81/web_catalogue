from django.urls import path
from web_shop_0_1.company_info.views import show_company_info, MessagesCreateView

urlpatterns = [
    path('contacts/', show_company_info, name='contact'),
    path('messages/', MessagesCreateView.as_view(), name='message')
]
